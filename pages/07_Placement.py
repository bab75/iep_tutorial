"""Step 7 — Placement & LRE"""
import streamlit as st, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
st.set_page_config(page_title="Step 7 · IEP Tutorial", page_icon="🏫", layout="wide")
from utils.engine import *
apply_theme(); init_session(); sidebar_nav()
page_header("🏫", "Step 7 — Placement & LRE", "The law requires the least restrictive appropriate setting")
step_badge(7)

scenario_box(
    "The IEP team has written Alex's goals and service recommendations. Now they must decide "
    "WHERE Alex will receive his education and services. Alex's parents want him to stay with "
    "his class as much as possible. The team must document what options were considered and "
    "why they chose this placement."
)

info_card(
    "Least Restrictive Environment (LRE)",
    "IDEA requires that students with disabilities be educated with non-disabled peers "
    "<b>to the maximum extent appropriate</b>. Removal from general education must be "
    "justified in writing. The continuum of placements ranges from full inclusion "
    "to home instruction — each step more restrictive than the last.",
    "#0891B2"
)
law_badge(
    "IDEA § 300.114",
    "Each public agency must ensure that to the maximum extent appropriate, children "
    "with disabilities are educated with children who are nondisabled."
)

# ── LRE Continuum ─────────────────────────────────────────────────────────────
st.markdown("### The LRE Continuum — Least to Most Restrictive")

placements = [
    (1, "General Education + Accommodations",
     "Student stays in the regular class all day with accommodations only. No specialized instruction from a special ed teacher.",
     "#16A34A", False),
    (2, "Consultant Teacher (CT)",
     "Special ed teacher advises the general ed teacher on how to support the student. Student remains in the general ed class.",
     "#0D9488", False),
    (3, "Resource Room",
     "Student is pulled out to a small group for specialized instruction in specific subjects. Spends most of the day in general ed.",
     "#2563EB", True),
    (4, "Integrated Co-Teaching (ICT)",
     "A general ed teacher and special ed teacher co-teach the same class. Up to 40% of students may have IEPs.",
     "#7C3AED", False),
    (5, "Special Class 12:1:1",
     "A separate classroom with only students who have IEPs. 12 students, 1 special ed teacher, 1 paraprofessional.",
     "#D97706", False),
    (6, "Special Class 8:1:1 or 6:1:1",
     "Smaller class ratio for students with higher support needs. More intensive individualized instruction.",
     "#E65100", False),
    (7, "Specialized School",
     "A separate school specifically designed for students with significant disabilities.",
     "#DC2626", False),
    (8, "Non-Public School (NPS)",
     "A private school approved by the state for students whose needs cannot be met in any public school program.",
     "#9F1239", False),
    (9, "Home Instruction",
     "Most restrictive. A teacher comes to the student's home. Temporary — for medical reasons only.",
     "#374151", False),
]

for level, name, desc, color, is_alex in placements:
    filled  = "▓" * level
    empty   = "░" * (9 - level)
    bar     = filled + empty
    bg      = "#EFF6FF" if is_alex else "white"
    border  = "2px solid #2563EB" if is_alex else "1px solid #E2E8F0"

    alex_badge = ""
    if is_alex:
        alex_badge = (
            '<span style="background:#2563EB;color:white;border-radius:4px;'
            'padding:1px 8px;font-size:0.68rem;font-weight:700;margin-left:8px;">'
            'Alex\'s placement</span>'
        )

    st.markdown(f"""
    <div style="display:flex;gap:12px;align-items:center;padding:10px 12px;
                margin-bottom:6px;background:{bg};border:{border};
                border-radius:10px;">
        <span style="font-family:monospace;color:{color};font-size:0.82rem;
                     min-width:82px;letter-spacing:2px;flex-shrink:0;">{bar}</span>
        <div style="flex:1;">
            <div style="font-weight:700;color:{color};font-size:0.87rem;">
                {name}{alex_badge}
            </div>
            <div style="color:#64748B;font-size:0.78rem;margin-top:3px;line-height:1.5;">
                {desc}
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown(
    "**Alex's placement:** Resource Room for ELA (reading and writing) + "
    "General Education for all other subjects. The team documented why full ICT "
    "was not appropriate and why resource room is the least restrictive option that "
    "meets his needs."
)

# ── Role tip ──────────────────────────────────────────────────────────────────
role_tips = {
    "Parent / Caregiver":
        "Ask the team: 'What less restrictive option was considered and why was it rejected?' "
        "The team must answer this in writing. If you disagree, say so at the meeting and "
        "ask that your disagreement be noted in the minutes. You can challenge placement "
        "through mediation.",
    "Special Education Teacher":
        "Document your LRE analysis for every recommendation. You must show what less "
        "restrictive settings were considered and specifically why they are not appropriate "
        "for this student.",
    "CSE Coordinator / Administrator":
        "The LRE justification must be explicit in the IEP. 'This is the appropriate "
        "placement' is not enough — document what less restrictive options were considered "
        "and why each was rejected.",
    "General Education Teacher":
        "Your input on whether supplementary aids and services could support the student "
        "in your classroom is critical to the LRE analysis. Be specific about what you "
        "have tried and what additional supports you would need.",
}
role_tip(role_tips.get(
    get_role(),
    "Every placement decision must document why a less restrictive setting was not appropriate."
))

# ── Decision branch ───────────────────────────────────────────────────────────
st.markdown("## 🔀 Decision Point — Parent Wants More Inclusion")
scenario_box(
    "Alex's parents want him to stay in the general education classroom full time with "
    "an ICT model. The team recommends Resource Room. Alex's parents disagree and say "
    "they do not want their son pulled out of class. What is the right next step?"
)

choice = st.radio(
    "What should happen?",
    [
        "A) The school's recommendation overrides the parent's preference — they are the experts",
        "B) The parent can note their disagreement in the IEP and pursue mediation",
        "C) The parent must accept placement or withdraw the child from the school",
        "D) The IEP cannot be finalized at all until both sides agree",
    ],
    label_visibility="collapsed",
    key="s7_branch",
)

if choice:
    if choice.startswith("B"):
        st.success(
            "✅ Correct! Parents have the right to disagree with placement and have that "
            "disagreement documented in the IEP. They can then request free mediation or "
            "file a due process complaint. The Stay Put rule means Alex continues in his "
            "current placement while any dispute is being resolved."
        )
    elif choice.startswith("A"):
        st.error(
            "❌ Not correct. Parents are equal members of the IEP team. The school cannot "
            "simply override a parent's disagreement. The parent has the right to challenge "
            "the placement decision through formal dispute resolution."
        )
    elif choice.startswith("C"):
        st.error(
            "❌ Not correct. Withdrawing is the most drastic option and almost never "
            "necessary. Parents have multiple free options — mediation, state complaint, "
            "due process — before considering withdrawal."
        )
    else:
        st.error(
            "❌ Not quite. If the team cannot reach consensus, the school makes the "
            "placement decision — but documents the parent's disagreement. The IEP can "
            "be finalized with a recorded disagreement. The parent retains full rights "
            "to challenge it."
        )

# ── Key facts ─────────────────────────────────────────────────────────────────
st.markdown("## Key Facts About Placement")
facts = [
    ("LRE is a requirement, not a preference",
     "The school must place the student in the least restrictive environment where "
     "they can receive an appropriate education — not the most convenient setting."),
    ("Justification must be in writing",
     "If the team recommends a more restrictive setting, the IEP must document what "
     "less restrictive option was considered and why it was rejected."),
    ("Stay Put during disputes",
     "If a parent challenges a placement decision, the student stays in their current "
     "placement until the dispute is fully resolved — no changes without consent."),
    ("Placement is reviewed annually",
     "At every annual review, the team reconsiders whether the current placement is "
     "still the least restrictive appropriate option. Students can move to less "
     "restrictive settings as they make progress."),
]
for title, desc in facts:
    st.markdown(f"""
    <div style="display:flex;gap:10px;padding:8px 0;border-bottom:1px solid #F1F5F9;
                align-items:flex-start;">
        <span style="color:#0891B2;font-size:1rem;flex-shrink:0;margin-top:2px;">▸</span>
        <div>
            <span style="font-weight:700;color:#1E293B;font-size:0.87rem;">{title}:</span>
            <span style="color:#475569;font-size:0.87rem;"> {desc}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ── Quiz ──────────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown("## 📝 Knowledge Check")
render_quiz(7, [
    {
        "q": "What does LRE mean in practice for Alex?",
        "options": [
            "Alex must be in a general education class all day",
            "Alex must be in a special class all day",
            "Alex must be educated with non-disabled peers to the maximum extent appropriate",
            "Alex's placement is decided solely by the principal",
        ],
        "correct": 2,
        "explanation":
            "LRE means the most inclusive setting where the student can receive an appropriate "
            "education with needed supports. It is a continuum — not all-or-nothing.",
        "wrong_msg":
            "LRE is not binary. It means the least restrictive setting where the student can "
            "genuinely make progress. Too restrictive violates IDEA; too permissive without "
            "support also fails the student.",
    },
    {
        "q": "What must the IEP document about placement?",
        "options": [
            "Only the placement that was chosen",
            "The chosen placement AND why less restrictive options were rejected",
            "Only the parent's preference",
            "A cost comparison of all placement options",
        ],
        "correct": 1,
        "explanation":
            "The IEP must include the LRE justification — both the chosen placement and "
            "the reason why less restrictive options are not appropriate.",
        "wrong_msg":
            "Documentation must include the reasoning. This protects the student from "
            "being placed in an unnecessarily restrictive setting.",
    },
    {
        "q": "During a placement dispute, what happens to Alex's current program?",
        "options": [
            "All services stop until the dispute is resolved",
            "Alex moves to the school's preferred placement immediately",
            "Alex stays in his current placement — the Stay Put rule applies",
            "The parent must agree to any interim changes",
        ],
        "correct": 2,
        "explanation":
            "Stay Put means the child remains in their current educational placement "
            "during any pending dispute. Nothing changes without parental consent.",
        "wrong_msg":
            "Stay Put is one of the strongest parent protections in IDEA. During any "
            "dispute, the student's current placement is frozen.",
    },
])
