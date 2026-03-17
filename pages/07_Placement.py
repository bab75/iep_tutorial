"""Step 7 — Placement & LRE"""
import streamlit as st, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
st.set_page_config(page_title="Step 7 · IEP Tutorial", page_icon="🏫", layout="wide")
from utils.engine import *
apply_theme(); init_session(); sidebar_nav()
page_header("🏫", "Step 7 — Placement & LRE", "The law requires the least restrictive appropriate setting")
step_badge(7)

scenario_box("The IEP team has written Alex's goals and service recommendations. Now they must decide WHERE Alex will receive his education and services. Alex's parents want him to stay with his class as much as possible. The team must document what options were considered and why they chose this placement.")

info_card("Least Restrictive Environment (LRE)",
    "IDEA requires that students with disabilities be educated with non-disabled peers "
    "<b>to the maximum extent appropriate</b>. Removal from general education must be "
    "justified in writing. The continuum of placements ranges from full inclusion "
    "to home instruction — each step more restrictive than the last.",
    "#0891B2")
law_badge("IDEA § 300.114", "Each public agency must ensure that to the maximum extent appropriate, children with disabilities are educated with children who are nondisabled.")

st.markdown("## The LRE Continuum — Least to Most Restrictive")
placements = [
    (1, "General Education + Accommodations", "Student stays in regular class with accommodations only. No special ed instruction.", "#16A34A"),
    (2, "Consultant Teacher (CT)", "Special ed teacher consults with gen ed teacher. Student stays in class.", "#0D9488"),
    (3, "Resource Room", "Student pulled out for specialized instruction in small group. Mostly in gen ed.", "#2563EB"),
    (4, "Integrated Co-Teaching (ICT)", "Two teachers co-teach one class. Up to 40% students with IEPs.", "#7C3AED"),
    (5, "Special Class 12:1:1", "Separate class, all students with IEPs. 12 students, 1 teacher, 1 para.", "#D97706"),
    (6, "Special Class 8:1:1 or 6:1:1", "Smaller ratio for higher support needs.", "#E65100"),
    (7, "Specialized School (District 75 equivalent)", "Separate school for students with significant disabilities.", "#DC2626"),
    (8, "Non-Public School (NPS)", "Private approved school for needs that cannot be met in public school.", "#9F1239"),
    (9, "Home Instruction", "Most restrictive. Temporary, for medical reasons only.", "#374151"),
]
for level, name, desc, color in placements:
    bar = "▓" * level + "░" * (9 - level)
    highlight = level == 3  # Alex's placement
    st.markdown(f"""
    <div style="display:flex;gap:10px;align-items:center;padding:8px 0;
                border-bottom:1px solid #F1F5F9;
                {'background:#EFF6FF;border-radius:8px;padding:8px 10px;margin-bottom:2px;' if highlight else ''}">
        <span style="font-family:monospace;color:{color};font-size:0.75rem;
                     min-width:90px;letter-spacing:1px;">{bar}</span>
        <div style="flex:1;">
            <span style="font-weight:700;color:{color};font-size:0.82rem;">{name}</span>
            {' <span style="background:#2563EB;color:white;border-radius:4px;padding:1px 6px;font-size:0.68rem;font-weight:700;">← Alex\'s placement</span>' if highlight else ''}
            <div style="color:#64748B;font-size:0.78rem;margin-top:1px;">{desc}</div>
        </div>
    </div>""", unsafe_allow_html=True)

st.markdown("**Alex's placement:** Resource Room for ELA (reading/writing) + General Education for all other subjects. The team documented why full ICT was not appropriate and why resource room was the least restrictive appropriate option.")

role_tip({
    "Parent / Caregiver": "Ask the team: 'What less restrictive option was considered and why was it rejected?' The team must answer this in writing. If you disagree with placement, Say so at the meeting and ask it be noted. You can challenge placement through mediation.",
    "Special Education Teacher": "Document your LRE analysis. For every placement recommendation, you must show what was considered and why the more restrictive setting is necessary.",
    "CSE Coordinator / Administrator": "The LRE justification must be explicit in the IEP. 'This is the appropriate placement' is not sufficient — you must document what less restrictive options were considered.",
    "General Education Teacher": "Your input about whether supplementary aids and services could support the student in general education is critical to the LRE analysis.",
}.get(get_role(), "Every placement decision must document why a less restrictive setting was not appropriate."))

st.markdown("## 🔀 Decision Point — Parent Wants More Inclusion")
scenario_box("Alex's parents want him to stay in the general education classroom full time with an ICT model. The team recommends Resource Room. Alex's parents disagree. What is the right next step?")
choice = st.radio("What should happen?", [
    "A) The school's recommendation overrides the parent's preference",
    "B) The parent can note their disagreement, request it be in the IEP, and pursue mediation",
    "C) The parent must accept placement or withdraw the child",
    "D) The IEP cannot be finalized until all parties agree",
], label_visibility="collapsed", key="s7_branch")
if choice:
    if choice.startswith("B"):
        st.success("✅ Correct! Parents have the right to disagree with placement and document that disagreement. They can request mediation (free) or file a due process complaint. Meanwhile, Stay Put means Alex continues in his current placement until the dispute is resolved.")
    elif choice.startswith("A"):
        st.error("❌ Not correct. Parents are equal members of the IEP team. While the team makes the decision collaboratively, a parent has the right to disagree and challenge the decision.")
    elif choice.startswith("C"):
        st.error("❌ Not correct. Parents have multiple options to challenge placement — mediation, state complaint, due process. Withdrawing the child is the most drastic option and rarely necessary.")
    else:
        st.error("❌ Not quite. If the team cannot reach consensus, the school makes the placement decision — but the parent retains the right to challenge it. The IEP can be finalized even with a documented disagreement.")

st.markdown("---")
st.markdown("## 📝 Knowledge Check")
render_quiz(7, [
    {"q": "What does LRE mean in practice for Alex?",
     "options": [
         "Alex must be in a general education class all day",
         "Alex must be in a special class all day",
         "Alex must be educated with non-disabled peers to the maximum extent appropriate",
         "Alex's placement is decided by the principal alone",
     ], "correct": 2,
     "explanation": "LRE means maximum inclusion that is appropriate for the student. It is not all-or-nothing — it means the least restrictive setting where the student can make meaningful progress.",
     "wrong_msg": "LRE is a continuum, not a binary choice. It means the most inclusive setting where the student can receive an appropriate education with needed supports."},
    {"q": "What must the IEP document about placement?",
     "options": [
         "Only the chosen placement",
         "The chosen placement and why less restrictive options were rejected",
         "Only the parent's preference",
         "A comparison of all 9 placement levels",
     ], "correct": 1,
     "explanation": "The IEP must document both the placement chosen AND why less restrictive options were not appropriate. This is the LRE justification.",
     "wrong_msg": "Documentation must include the reasoning — why less restrictive settings were not chosen. This protects against arbitrary placement decisions."},
    {"q": "During a placement dispute, what happens to Alex's current program?",
     "options": [
         "Services stop until the dispute is resolved",
         "Alex moves to the school's preferred placement immediately",
         "Alex stays in his current placement — the Stay Put rule applies",
         "The parent must agree to any changes",
     ], "correct": 2,
     "explanation": "During any dispute, the Stay Put rule means the child continues in their current educational placement. No changes can be made without parental consent while a dispute is pending.",
     "wrong_msg": "Stay Put is a critical parent protection. During a dispute, nothing changes without the parent's agreement."},
])
