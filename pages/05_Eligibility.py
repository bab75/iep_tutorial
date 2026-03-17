"""Step 5 — Eligibility"""
import streamlit as st, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
st.set_page_config(page_title="Step 5 · IEP Tutorial", page_icon="⚖️", layout="wide")
from utils.engine import *
apply_theme(); init_session(); sidebar_nav()
page_header("⚖️", "Step 5 — Eligibility", "The team meets to decide if the student qualifies — and you are on the team")
step_badge(5)

scenario_box("All of Alex's evaluations are complete. The psychoeducational report shows a significant gap between Alex's cognitive ability (average) and his reading and writing achievement (well below average). The SLP finds a language processing weakness. The team — including Alex's parents — meets to review all findings and determine if Alex qualifies for special education.")

info_card("The Eligibility Meeting", "The eligibility determination is made by the <b>full IEP team</b> — which includes the parent as an equal member. No single professional makes the decision alone. The team reviews all evaluation data and votes on eligibility.", "#DC2626")
law_badge("IDEA § 300.306", "The team must determine eligibility based on the evaluation results and must not use any single measure as the sole criterion.")

st.markdown("## The 13 IDEA Disability Categories")
cats = [
    ("Specific Learning Disability (SLD)", "Most common. Includes dyslexia, dyscalculia, dysgraphia.", "#2563EB"),
    ("Speech or Language Impairment", "Articulation, language, fluency disorders.", "#0D9488"),
    ("Other Health Impairment (OHI)", "Includes ADHD, chronic health conditions.", "#7C3AED"),
    ("Autism Spectrum Disorder", "Wide range of communication and social differences.", "#D97706"),
    ("Emotional Disturbance", "Mental health conditions affecting learning.", "#DC2626"),
    ("Intellectual Disability", "Significant limitations in cognitive and adaptive functioning.", "#16A34A"),
    ("Hearing Impairment / Deafness", "Mild to severe hearing loss, or total deafness.", "#0891B2"),
    ("Visual Impairment / Blindness", "Even when corrected, affects educational performance.", "#9333EA"),
    ("Orthopedic Impairment", "Physical impairments affecting school access.", "#E65100"),
    ("Traumatic Brain Injury (TBI)", "Acquired brain injury from external force.", "#7F1D1D"),
    ("Multiple Disabilities", "Two or more disabilities together.", "#4A1B9A"),
    ("Deaf-Blindness", "Combination of hearing and visual impairments.", "#1E3A5F"),
    ("Developmental Delay", "For children ages 3-9 only.", "#374151"),
]
cols = st.columns(3)
for i, (name, desc, color) in enumerate(cats):
    with cols[i % 3]:
        st.markdown(f"""
        <div style="background:white;border-left:3px solid {color};border-radius:7px;
                    padding:8px 10px;margin-bottom:6px;">
            <div style="font-weight:700;color:{color};font-size:0.75rem;">{name}</div>
            <div style="color:#64748B;font-size:0.72rem;margin-top:2px;">{desc}</div>
        </div>""", unsafe_allow_html=True)

st.markdown("**Alex qualifies under:** Specific Learning Disability (SLD) — the evaluation shows the required discrepancy between ability and achievement in reading and written expression.")

role_tip({
    "Parent / Caregiver": "You are an equal voting member of the eligibility team. Bring your own observations and any outside evaluations or reports. Your input must be considered.",
    "Special Education Teacher": "Present the evaluation findings clearly. Use plain language — parents should understand every data point discussed. Avoid jargon.",
    "CSE Coordinator / Administrator": "Document all team members present, all data reviewed, and the team's rationale for the eligibility decision.",
    "General Education Teacher": "Your input about classroom performance is critical. Come prepared with specific examples, grades, and observations.",
}.get(get_role(), "The parent is an equal member of the eligibility team."))

st.markdown("## 🔀 Decision Point — Student NOT Found Eligible")
scenario_box("Imagine the team reviews the data and determines Alex does NOT meet the criteria for any disability category. His scores, while low, are consistent with his cognitive ability. What options does Alex's family have?")
choice = st.radio("What can the family do?", [
    "A) Nothing — the team's decision is final and cannot be challenged",
    "B) Request an IEE, ask for a 504 Plan, and/or request a due process hearing",
    "C) Wait until next year and re-refer",
    "D) Request the general education teacher provide more help",
], label_visibility="collapsed", key="s5_branch")
if choice:
    if choice.startswith("B"):
        st.success("✅ Correct! If the family disagrees with the eligibility decision they can: (1) Request an IEE at school expense, (2) Explore a 504 Plan for accommodations, (3) Request mediation or a due process hearing. They do not have to accept the team's decision.")
    elif choice.startswith("A"):
        st.error("❌ Not correct. Parents have extensive rights to challenge eligibility decisions. Accepting an ineligibility finding without question is not required.")
    elif choice.startswith("C"):
        st.error("❌ Not the best first step. Waiting a year delays services Alex may need. There are immediate options available.")
    else:
        st.error("❌ While classroom support is helpful, it does not address the family's right to challenge the eligibility decision or obtain a 504 Plan.")

st.markdown("---")
st.markdown("## 📝 Knowledge Check")
render_quiz(5, [
    {"q": "Who makes the eligibility determination?",
     "options": [
         "The school psychologist alone",
         "The CSE chairperson",
         "The full IEP team including the parent",
         "The principal",
     ], "correct": 2,
     "explanation": "Eligibility is a team decision. The parent is a required member of that team and has an equal vote.",
     "wrong_msg": "No single person decides eligibility. It is a team decision that must include the parent."},
    {"q": "Alex qualifies under which disability category?",
     "options": [
         "Other Health Impairment",
         "Autism Spectrum Disorder",
         "Specific Learning Disability",
         "Emotional Disturbance",
     ], "correct": 2,
     "explanation": "Alex shows a significant discrepancy between cognitive ability and academic achievement in reading and writing — the core criteria for Specific Learning Disability.",
     "wrong_msg": "Based on Alex's profile — average IQ but significantly below-average reading and writing — Specific Learning Disability is the appropriate classification."},
    {"q": "A parent receives an ineligibility decision. What is their FIRST right?",
     "options": [
         "Accept the decision and monitor at home",
         "Request an Independent Educational Evaluation at school expense",
         "Remove the child from school",
         "Contact the teacher",
     ], "correct": 1,
     "explanation": "If a parent disagrees with the evaluation that led to ineligibility, their first step is requesting an IEE at public expense.",
     "wrong_msg": "An IEE is the primary tool for challenging evaluation findings. The school must pay for it or immediately file for a hearing."},
])
