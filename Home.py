"""
IEP Tutorial — Home
Role selector, tutorial overview, progress dashboard.
"""
import streamlit as st
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

st.set_page_config(
    page_title="IEP Tutorial",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)

from utils.engine import (
    init_session, apply_theme, sidebar_nav,
    ROLES, STEPS, TOTAL_STEPS,
    steps_completed, overall_progress, get_step_score, is_step_complete,
)

apply_theme()
init_session()
sidebar_nav()

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="background:linear-gradient(135deg,#1E3A8A 0%,#1D4ED8 100%);
            border-radius:16px;padding:28px 32px;margin-bottom:24px;
            position:relative;overflow:hidden;">
    <div style="position:absolute;top:-30px;right:-20px;width:180px;height:180px;
                background:rgba(255,255,255,0.06);border-radius:50%;"></div>
    <div style="position:absolute;bottom:-40px;right:60px;width:120px;height:120px;
                background:rgba(255,255,255,0.04);border-radius:50%;"></div>
    <div style="position:relative;z-index:1;">
        <div style="font-size:2.5rem;margin-bottom:10px;">📚</div>
        <div style="font-family:'Nunito',sans-serif;font-weight:900;
                    font-size:1.9rem;color:white;line-height:1.2;margin-bottom:8px;">
            IEP Process Tutorial</div>
        <div style="color:rgba(255,255,255,0.85);font-size:0.95rem;max-width:600px;
                    line-height:1.7;">
            Learn the complete IEP process step by step — from identifying a student
            with a disability all the way through services, annual reviews, and what
            to do when things go wrong. Interactive scenarios, real decisions, instant feedback.
        </div>
        <div style="display:flex;gap:10px;flex-wrap:wrap;margin-top:14px;">
            <span style="background:rgba(255,255,255,0.15);color:white;border-radius:20px;
                         padding:4px 14px;font-size:0.8rem;font-weight:600;">
                ✅ 10 Learning Steps</span>
            <span style="background:rgba(255,255,255,0.15);color:white;border-radius:20px;
                         padding:4px 14px;font-size:0.8rem;font-weight:600;">
                🔀 Real Decision Scenarios</span>
            <span style="background:rgba(255,255,255,0.15);color:white;border-radius:20px;
                         padding:4px 14px;font-size:0.8rem;font-weight:600;">
                📋 Knowledge Quizzes</span>
            <span style="background:rgba(255,255,255,0.15);color:white;border-radius:20px;
                         padding:4px 14px;font-size:0.8rem;font-weight:600;">
                🎓 Completion Certificate</span>
            <span style="background:rgba(255,255,255,0.15);color:white;border-radius:20px;
                         padding:4px 14px;font-size:0.8rem;font-weight:600;">
                ⚖️ Based on Federal IDEA Law</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Role selector ─────────────────────────────────────────────────────────────
st.markdown("""
<div style="font-family:'Nunito',sans-serif;font-weight:800;
            font-size:1.1rem;color:#1E293B;margin:20px 0 6px;">
    Step 1 — Choose your role
</div>
<div style="color:#64748B;font-size:0.88rem;margin-bottom:14px;">
    The tutorial adapts its focus based on your role. You can change this at any time.
</div>
""", unsafe_allow_html=True)

role_cols = st.columns(4)
current_role = st.session_state.get("role")

for col, (role_name, rc) in zip(role_cols, ROLES.items()):
    with col:
        is_selected = current_role == role_name
        border = f"3px solid {rc['color']}" if is_selected else "2px solid #E2E8F0"
        bg     = rc["tip_color"] if is_selected else "white"
        st.markdown(f"""
        <div style="background:{bg};border:{border};border-radius:12px;
                    padding:16px;text-align:center;min-height:120px;
                    cursor:pointer;">
            <div style="font-size:2rem;margin-bottom:6px;">{rc['icon']}</div>
            <div style="font-family:'Nunito',sans-serif;font-weight:800;
                        color:{rc['color']};font-size:0.85rem;margin-bottom:4px;">
                {role_name}</div>
            <div style="color:#64748B;font-size:0.75rem;line-height:1.5;">
                {rc['focus']}</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button(
            "✓ Selected" if is_selected else "Select",
            key=f"role_{role_name[:10]}",
            use_container_width=True,
            type="primary" if is_selected else "secondary",
        ):
            st.session_state.role = role_name
            st.session_state.tutorial_started = True
            st.rerun()

if not current_role:
    st.info("👆 Select your role above to begin the tutorial.")
    st.stop()

# ── Progress dashboard (shown after role selected) ────────────────────────────
done = steps_completed()
pct  = int(overall_progress() * 100)

st.markdown(f"""
<div style="background:white;border:1px solid #E2E8F0;border-radius:14px;
            padding:20px 24px;margin:20px 0 16px;">
    <div style="display:flex;justify-content:space-between;align-items:center;
                flex-wrap:wrap;gap:10px;margin-bottom:12px;">
        <div style="font-family:'Nunito',sans-serif;font-weight:800;
                    color:#1E293B;font-size:1rem;">
            Your Progress</div>
        <span style="background:#EFF6FF;color:#1E40AF;border-radius:20px;
                     padding:4px 14px;font-size:0.8rem;font-weight:700;">
            {done} of {TOTAL_STEPS} steps complete · {pct}%</span>
    </div>
    <div style="background:#F1F5F9;border-radius:8px;height:10px;overflow:hidden;">
        <div style="background:linear-gradient(90deg,#2563EB,#0D9488);
                    height:100%;width:{pct}%;border-radius:8px;
                    transition:width 0.5s;"></div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Step overview grid ────────────────────────────────────────────────────────
st.markdown("""
<div style="font-family:'Nunito',sans-serif;font-weight:800;
            font-size:1rem;color:#1E293B;margin:16px 0 10px;">
    Tutorial Steps — use the sidebar to navigate
</div>
""", unsafe_allow_html=True)

step_colors = [
    "#2563EB","#0D9488","#7C3AED","#D97706","#DC2626",
    "#16A34A","#0891B2","#9333EA","#D97706","#1D4ED8","#16A34A"
]

rows = [STEPS[i:i+4] for i in range(0, len(STEPS), 4)]
for row in rows:
    cols = st.columns(len(row))
    for col, step in zip(cols, row):
        completed = is_step_complete(step["id"])
        score     = get_step_score(step["id"]) if completed else None
        color     = step_colors[step["id"] - 1]
        bg        = "#F0FDF4" if completed else "white"
        border_t  = f"4px solid {'#16A34A' if completed else color}"
        with col:
            st.markdown(f"""
            <div style="background:{bg};border-radius:12px;border:1px solid #E2E8F0;
                        border-top:{border_t};padding:14px;margin-bottom:10px;
                        min-height:100px;text-align:center;">
                <div style="font-size:1.5rem;margin-bottom:4px;">
                    {'✅' if completed else step['icon']}</div>
                <div style="font-family:'Nunito',sans-serif;font-weight:800;
                            color:{'#15803D' if completed else '#1E293B'};
                            font-size:0.78rem;margin-bottom:3px;">
                    Step {step['id']}</div>
                <div style="color:#64748B;font-size:0.74rem;line-height:1.4;">
                    {step['title']}</div>
                {f'<div style="color:#16A34A;font-size:0.72rem;font-weight:700;margin-top:4px;">{score}%</div>' if score is not None else ''}
            </div>
            """, unsafe_allow_html=True)

# ── Start / continue button ───────────────────────────────────────────────────
st.markdown("<div style='margin:20px 0 8px'></div>", unsafe_allow_html=True)

if done == 0:
    st.info("👈 Use the sidebar to navigate — start with **Step 1: Meet the Student**")
elif done == TOTAL_STEPS:
    st.success("🎉 You have completed all steps! Go to **Step 11: Certificate** to get your certificate.")
else:
    # Find next incomplete step
    next_step = next((s for s in STEPS if not is_step_complete(s["id"]) and s["id"] <= TOTAL_STEPS), None)
    if next_step:
        st.info(f"👈 Continue with **Step {next_step['id']}: {next_step['title']}** in the sidebar.")

# ── What you will learn ───────────────────────────────────────────────────────
with st.expander("📖 What you will learn in this tutorial"):
    st.markdown("""
    **Step 1 — Meet the Student**
    Introduction to Alex, an 8-year-old struggling in school. You learn how Child Find works
    and how the special education process is triggered.

    **Step 2 — Referral**
    Who can refer a student, what a referral looks like, what the school must do within
    5 school days, and what happens if the school ignores a concern.

    **Step 3 — Consent to Evaluate**
    What informed consent means, what happens when a parent refuses or delays,
    and how the 60-day clock starts the moment consent is signed.

    **Step 4 — Evaluation**
    The 12 types of evaluations, who conducts them, the multidisciplinary requirement,
    and what happens if the school misses the 60-day deadline.

    **Step 5 — Eligibility**
    The 13 IDEA disability categories, how the eligibility meeting works,
    what happens if the student is found ineligible, and parent rights at this stage.

    **Step 6 — IEP Meeting**
    Who must be on the IEP team, what gets written in the IEP, parent rights during
    the meeting, and what to do if the meeting happens without a parent.

    **Step 7 — Placement & LRE**
    The Least Restrictive Environment continuum, all placement options,
    what justification is required for more restrictive settings.

    **Step 8 — Consent & Mandates**
    IEP consent (different from evaluation consent), what mandates mean,
    when services must begin, and what happens if the parent refuses the IEP.

    **Step 9 — Annual Review**
    The annual IEP review cycle, the 3-year reevaluation, how to amend an IEP
    without a full meeting, and what happens if the review is missed.

    **Step 10 — Disputes & Resolution**
    All 4 dispute options side by side, the Stay Put rule, how to file a state
    complaint, and when to use due process.
    """)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center;color:#94A3B8;font-size:0.75rem;
            margin-top:32px;padding-top:12px;border-top:1px solid #E2E8F0;">
    IEP Process Tutorial · Based on IDEA Federal Law · Free to use
</div>
""", unsafe_allow_html=True)
