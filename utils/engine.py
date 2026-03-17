"""
IEP Tutorial — Core Engine
Manages session state, progress, scoring, and role configuration.
No API key. No external services. Pure Python.
"""
import streamlit as st

# ── Roles ─────────────────────────────────────────────────────────────────────
ROLES = {
    "Parent / Caregiver": {
        "icon":  "👨‍👩‍👧",
        "color": "#2563EB",
        "focus": "Your rights, what to watch for, and how to advocate for your child.",
        "tips_label": "Parent Tip",
        "tip_color": "#EFF6FF",
        "tip_border": "#2563EB",
    },
    "Special Education Teacher": {
        "icon":  "👩‍🏫",
        "color": "#0D9488",
        "focus": "Timelines, documentation responsibilities, and compliance requirements.",
        "tips_label": "Teacher Note",
        "tip_color": "#F0FDF4",
        "tip_border": "#0D9488",
    },
    "CSE Coordinator / Administrator": {
        "icon":  "📋",
        "color": "#7C3AED",
        "focus": "Process oversight, legal compliance, and team coordination.",
        "tips_label": "Coordinator Note",
        "tip_color": "#F5F3FF",
        "tip_border": "#7C3AED",
    },
    "General Education Teacher": {
        "icon":  "🏫",
        "color": "#D97706",
        "focus": "Your role in the IEP team and classroom responsibilities.",
        "tips_label": "Teacher Note",
        "tip_color": "#FFFBEB",
        "tip_border": "#D97706",
    },
}

# ── Tutorial steps ────────────────────────────────────────────────────────────
STEPS = [
    {"id": 1,  "title": "Meet the Student",         "icon": "👦", "page": "01_Student_Profile"},
    {"id": 2,  "title": "Referral",                 "icon": "✉️", "page": "02_Referral"},
    {"id": 3,  "title": "Consent to Evaluate",      "icon": "✍️", "page": "03_Consent"},
    {"id": 4,  "title": "Evaluation",               "icon": "🔬", "page": "04_Evaluation"},
    {"id": 5,  "title": "Eligibility",              "icon": "⚖️", "page": "05_Eligibility"},
    {"id": 6,  "title": "IEP Meeting",              "icon": "🤝", "page": "06_IEP_Meeting"},
    {"id": 7,  "title": "Placement & LRE",          "icon": "🏫", "page": "07_Placement"},
    {"id": 8,  "title": "Consent & Mandates",       "icon": "📋", "page": "08_Mandates"},
    {"id": 9,  "title": "Annual Review",            "icon": "🔄", "page": "09_Annual_Review"},
    {"id": 10, "title": "Disputes & Resolution",    "icon": "⚖️", "page": "10_Disputes"},
    {"id": 11, "title": "Certificate",              "icon": "🎓", "page": "11_Certificate"},
]

TOTAL_STEPS = 10  # steps 1-10 are learning steps; 11 is certificate


def init_session():
    """Initialize all session state defaults."""
    defaults = {
        "role":             None,
        "step_scores":      {},   # {step_id: score_pct}
        "step_completed":   set(),
        "quiz_answers":     {},   # {step_id: {q_idx: chosen}}
        "current_step":     1,
        "tutorial_started": False,
        "total_score":      0,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


def get_role():
    return st.session_state.get("role")


def get_role_config():
    role = get_role()
    return ROLES.get(role, ROLES["Parent / Caregiver"])


def mark_step_complete(step_id: int, score_pct: float):
    st.session_state.step_completed.add(step_id)
    st.session_state.step_scores[step_id] = score_pct
    # Recalculate total
    scores = list(st.session_state.step_scores.values())
    st.session_state.total_score = int(sum(scores) / len(scores)) if scores else 0


def is_step_complete(step_id: int) -> bool:
    return step_id in st.session_state.step_completed


def get_step_score(step_id: int) -> int:
    return int(st.session_state.step_scores.get(step_id, 0))


def steps_completed() -> int:
    return len(st.session_state.step_completed)


def overall_progress() -> float:
    return steps_completed() / TOTAL_STEPS


# ── Quiz engine ───────────────────────────────────────────────────────────────

def render_quiz(step_id: int, questions: list, on_complete=None):
    """
    Render a quiz for a step.
    questions = [
      {
        "q": "Question text",
        "options": ["A", "B", "C", "D"],
        "correct": 0,   # index of correct answer
        "explanation": "Why this is correct...",
        "wrong_msg": "Why the other options are wrong..."
      }
    ]
    Returns True if quiz was just completed this run.
    """
    rc   = get_role_config()
    key  = f"quiz_{step_id}"
    done_key = f"quiz_done_{step_id}"

    if st.session_state.get(done_key):
        score = get_step_score(step_id)
        st.markdown(f"""
        <div style="background:#F0FDF4;border:1px solid #86EFAC;border-radius:10px;
                    padding:14px 18px;margin:12px 0;">
            <div style="font-weight:700;color:#15803D;font-size:0.9rem;">
                ✅ Quiz completed — you scored {score}%</div>
            <div style="color:#166534;font-size:0.82rem;margin-top:4px;">
                Move to the next step using the sidebar.</div>
        </div>
        """, unsafe_allow_html=True)
        return False

    st.markdown(f"""
    <div style="background:{rc['tip_color']};border-left:4px solid {rc['tip_border']};
                border-radius:8px;padding:12px 16px;margin:16px 0 8px;">
        <div style="font-weight:700;color:{rc['tip_border']};font-size:0.82rem;
                    text-transform:uppercase;letter-spacing:.05em;margin-bottom:4px;">
            Knowledge Check — {len(questions)} Questions</div>
        <div style="color:#334155;font-size:0.85rem;">
            Answer all questions to complete this step and earn your badge.</div>
    </div>
    """, unsafe_allow_html=True)

    answers = st.session_state.quiz_answers.setdefault(step_id, {})
    all_answered = True

    for i, q in enumerate(questions):
        st.markdown(f"""
        <div style="font-weight:700;color:#1E293B;font-size:0.9rem;
                    margin:14px 0 8px;">Q{i+1}. {q['q']}</div>
        """, unsafe_allow_html=True)

        chosen = st.radio(
            f"q{step_id}_{i}",
            q["options"],
            index=answers.get(i, None),
            label_visibility="collapsed",
            key=f"radio_{step_id}_{i}",
        )

        if chosen is not None:
            answers[i] = q["options"].index(chosen)
            chosen_idx = q["options"].index(chosen)
            if chosen_idx == q["correct"]:
                st.markdown(f"""
                <div style="background:#F0FDF4;border-radius:6px;padding:8px 12px;
                            font-size:0.84rem;color:#15803D;">
                    ✅ Correct! {q['explanation']}</div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style="background:#FEF2F2;border-radius:6px;padding:8px 12px;
                            font-size:0.84rem;color:#DC2626;">
                    ❌ Not quite. {q['wrong_msg']}</div>
                """, unsafe_allow_html=True)
        else:
            all_answered = False

    if all_answered and answers:
        correct = sum(1 for i, q in enumerate(questions)
                      if answers.get(i) == q["correct"])
        score_pct = round(correct / len(questions) * 100)

        if st.button("✅  Submit Quiz & Complete Step", type="primary",
                     key=f"submit_{step_id}"):
            mark_step_complete(step_id, score_pct)
            st.session_state[done_key] = True
            if on_complete:
                on_complete()
            st.rerun()

    return False


# ── UI helpers ────────────────────────────────────────────────────────────────

def page_header(icon: str, title: str, subtitle: str):
    rc = get_role_config()
    color = rc["color"]
    st.markdown(f"""
    <div style="background:linear-gradient(135deg,{color} 0%,{color}cc 100%);
                border-radius:16px;padding:24px 28px;margin-bottom:20px;
                position:relative;overflow:hidden;">
        <div style="position:absolute;top:-20px;right:-20px;width:120px;height:120px;
                    background:rgba(255,255,255,0.07);border-radius:50%;"></div>
        <div style="position:relative;z-index:1;">
            <div style="font-size:2rem;margin-bottom:6px;">{icon}</div>
            <div style="font-family:'Nunito',sans-serif;font-weight:900;
                        font-size:1.5rem;color:white;line-height:1.2;margin-bottom:4px;">
                {title}</div>
            <div style="color:rgba(255,255,255,0.85);font-size:0.88rem;">{subtitle}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def role_tip(text: str, label: str = None):
    rc  = get_role_config()
    lbl = label or rc["tips_label"]
    st.markdown(f"""
    <div style="background:{rc['tip_color']};border-left:4px solid {rc['tip_border']};
                border-radius:8px;padding:12px 16px;margin:10px 0;">
        <div style="font-weight:700;color:{rc['tip_border']};font-size:0.78rem;
                    text-transform:uppercase;letter-spacing:.05em;margin-bottom:4px;">
            {rc['icon']} {lbl}</div>
        <div style="color:#334155;font-size:0.87rem;line-height:1.7;">{text}</div>
    </div>
    """, unsafe_allow_html=True)


def info_card(title: str, body: str, color: str = "#2563EB"):
    st.markdown(f"""
    <div style="background:white;border:1px solid #E2E8F0;border-left:5px solid {color};
                border-radius:10px;padding:14px 18px;margin:8px 0;">
        <div style="font-weight:700;color:{color};font-size:0.85rem;margin-bottom:6px;">
            {title}</div>
        <div style="color:#374151;font-size:0.88rem;line-height:1.75;">{body}</div>
    </div>
    """, unsafe_allow_html=True)


def scenario_box(scenario: str, color: str = "#D97706"):
    st.markdown(f"""
    <div style="background:#FFFBEB;border:2px solid {color};border-radius:12px;
                padding:16px 20px;margin:14px 0;">
        <div style="font-weight:700;color:{color};font-size:0.82rem;
                    text-transform:uppercase;letter-spacing:.05em;margin-bottom:8px;">
            📖 Scenario</div>
        <div style="color:#334155;font-size:0.92rem;line-height:1.8;
                    font-style:italic;">{scenario}</div>
    </div>
    """, unsafe_allow_html=True)


def law_badge(citation: str, text: str):
    st.markdown(f"""
    <div style="background:#EFF6FF;border-radius:8px;padding:10px 14px;
                margin:8px 0;display:flex;gap:10px;align-items:flex-start;">
        <span style="background:#2563EB;color:white;border-radius:5px;
                     padding:2px 8px;font-size:0.72rem;font-weight:700;
                     white-space:nowrap;margin-top:2px;">⚖️ {citation}</span>
        <span style="color:#1E40AF;font-size:0.84rem;line-height:1.65;">{text}</span>
    </div>
    """, unsafe_allow_html=True)


def step_badge(step_id: int):
    if is_step_complete(step_id):
        score = get_step_score(step_id)
        st.markdown(f"""
        <div style="display:inline-flex;align-items:center;gap:6px;
                    background:#F0FDF4;border:1px solid #86EFAC;border-radius:20px;
                    padding:4px 14px;font-size:0.8rem;font-weight:700;color:#15803D;">
            ✅ Step Complete · Score: {score}%
        </div>
        """, unsafe_allow_html=True)


def apply_theme():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&family=Nunito+Sans:wght@400;600&display=swap');
    html, body, [class*="css"] { font-family: 'Nunito Sans', sans-serif !important; }
    .stApp { background: #F8FAFF !important; }
    .main .block-container { padding: 1.5rem 2rem 3rem !important; max-width: 1000px !important; }
    [data-testid="stSidebar"] { background: linear-gradient(180deg,#1E3A8A 0%,#1D4ED8 100%) !important; }
    [data-testid="stSidebar"] * { color: #DBEAFE !important; }
    [data-testid="stSidebarNav"] a { font-family:'Nunito',sans-serif !important; font-weight:600 !important;
        font-size:0.88rem !important; padding:8px 12px !important; border-radius:8px !important;
        margin:2px 4px !important; transition:all 0.2s !important; }
    [data-testid="stSidebarNav"] a:hover { background:rgba(255,255,255,0.15) !important; }
    [data-testid="stSidebarNav"] a[aria-current="page"] {
        background:rgba(255,255,255,0.2) !important; border-left:3px solid #FCD34D !important; }
    .stButton > button { font-family:'Nunito',sans-serif !important; font-weight:700 !important;
        border-radius:10px !important; transition:all 0.2s !important; }
    .stRadio > div { gap: 6px !important; }
    .stRadio label { background:white; border:1px solid #E2E8F0; border-radius:8px;
        padding:8px 14px !important; font-size:0.88rem !important; cursor:pointer; }
    [data-testid="metric-container"] { background:white !important; border-radius:12px !important;
        padding:14px !important; border:1px solid #E2E8F0 !important; }
    #MainMenu, footer, header { visibility: hidden !important; }
    </style>
    """, unsafe_allow_html=True)


def sidebar_nav():
    """Render progress and navigation in sidebar."""
    with st.sidebar:
        role = get_role()
        rc   = get_role_config()

        st.markdown(f"""
        <div style="padding:14px 10px 20px;">
            <div style="font-size:1.4rem;margin-bottom:4px;">📚</div>
            <div style="font-family:'Nunito',sans-serif;font-weight:900;
                        font-size:1rem;color:white;line-height:1.3;">
                IEP Tutorial</div>
            <div style="font-size:0.78rem;color:rgba(255,255,255,0.65);margin-top:2px;">
                Interactive Learning Guide</div>
        </div>
        """, unsafe_allow_html=True)

        if role:
            st.markdown(f"""
            <div style="background:rgba(255,255,255,0.12);border-radius:8px;
                        padding:8px 12px;margin:0 6px 14px;">
                <div style="font-size:0.72rem;color:rgba(255,255,255,0.6);margin-bottom:2px;">
                    Your role</div>
                <div style="font-weight:700;color:white;font-size:0.85rem;">
                    {rc['icon']} {role}</div>
            </div>
            """, unsafe_allow_html=True)

        # Progress
        done  = steps_completed()
        total = TOTAL_STEPS
        pct   = int(done / total * 100)
        st.markdown(f"""
        <div style="padding:0 6px;margin-bottom:14px;">
            <div style="display:flex;justify-content:space-between;
                        font-size:0.75rem;color:rgba(255,255,255,0.7);margin-bottom:5px;">
                <span>Progress</span><span>{done}/{total} steps</span>
            </div>
            <div style="background:rgba(255,255,255,0.2);border-radius:6px;height:7px;">
                <div style="background:#FCD34D;height:100%;width:{pct}%;
                            border-radius:6px;transition:width 0.4s;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Step list
        st.markdown("""
        <div style="font-size:0.7rem;color:rgba(255,255,255,0.5);
                    text-transform:uppercase;letter-spacing:.06em;
                    padding:0 10px;margin-bottom:6px;">Steps</div>
        """, unsafe_allow_html=True)

        for step in STEPS:
            done_step = is_step_complete(step["id"])
            score_txt = f" · {get_step_score(step['id'])}%" if done_step else ""
            indicator = "✅" if done_step else step["icon"]
            st.markdown(f"""
            <div style="display:flex;align-items:center;gap:8px;
                        padding:5px 10px;font-size:0.8rem;
                        color:{'#FCD34D' if done_step else 'rgba(255,255,255,0.75)'};">
                <span style="font-size:0.85rem;">{indicator}</span>
                <span>{step['title']}{score_txt}</span>
            </div>
            """, unsafe_allow_html=True)

        if done == TOTAL_STEPS:
            st.markdown("""
            <div style="background:#FCD34D;border-radius:8px;padding:10px 12px;
                        margin:14px 6px 0;text-align:center;">
                <div style="font-weight:700;color:#1E3A8A;font-size:0.85rem;">
                    🎓 Tutorial Complete!</div>
                <div style="color:#1E40AF;font-size:0.75rem;margin-top:2px;">
                    View your certificate</div>
            </div>
            """, unsafe_allow_html=True)
