"""Step 4 — Evaluation"""
import streamlit as st
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
st.set_page_config(page_title="Step 4 · IEP Tutorial", page_icon="🔬", layout="wide")
from utils.engine import *
apply_theme(); init_session(); sidebar_nav()
page_header("🔬", "Step 4 — Evaluation", "A team of specialists evaluates every area of suspected disability")
step_badge(4)

scenario_box(
    "After Alex's mother signs consent on March 5th, the evaluation team swings into action. "
    "A school psychologist conducts cognitive and academic testing. A speech-language pathologist "
    "assesses Alex's language processing. His teacher completes rating scales. The social worker "
    "reviews school records. Alex's parents fill out a behavior questionnaire. "
    "All results must be compiled before the IEP meeting."
)

st.markdown("## The Multi-Disciplinary Evaluation")
info_card("Key Rule: No Single Test Can Determine Eligibility",
    "IDEA requires that evaluations be <b>multidisciplinary</b> — conducted by a team, "
    "using multiple tools and measures, in all areas of suspected disability. "
    "No single test score can be the sole basis for an eligibility decision.",
    "#7C3AED")

law_badge("IDEA § 300.304", "The school must use technically sound instruments and assess the child in all areas related to the suspected disability.")

# ── Evaluation types ──────────────────────────────────────────────────────────
st.markdown("## Common Evaluation Types")
evals = [
    ("🧠", "Psychoeducational", "IQ, academic achievement, processing. Done by school psychologist. Core of most evaluations.", "#2563EB"),
    ("🗣️", "Speech-Language", "Articulation, language comprehension, expressive language. Done by SLP.", "#0D9488"),
    ("✋", "Occupational Therapy", "Fine motor, sensory, handwriting. Done by OT.", "#7C3AED"),
    ("🏃", "Physical Therapy", "Gross motor, mobility. Done by PT.", "#D97706"),
    ("👁️", "Behavioral (FBA)", "Why challenging behavior occurs. Must be done before a BIP.", "#DC2626"),
    ("👂", "Audiological", "Hearing assessment. Done by audiologist.", "#16A34A"),
    ("💻", "Assistive Technology", "What devices could help. Required to be considered in every IEP.", "#0891B2"),
    ("💼", "Vocational", "Work interests and aptitudes. Required for transition planning at age 14+.", "#9333EA"),
]
cols = st.columns(4)
for i, (icon, name, desc, color) in enumerate(evals):
    with cols[i % 4]:
        st.markdown(f"""
        <div style="background:white;border-left:4px solid {color};border-radius:8px;
                    padding:10px;margin-bottom:8px;min-height:100px;">
            <div style="font-size:1.2rem;margin-bottom:4px;">{icon}</div>
            <div style="font-weight:700;color:{color};font-size:0.78rem;">{name}</div>
            <div style="color:#64748B;font-size:0.72rem;line-height:1.4;margin-top:2px;">{desc}</div>
        </div>""", unsafe_allow_html=True)

role_tip({
    "Parent / Caregiver": "Request copies of ALL evaluation reports BEFORE the eligibility meeting. You have the right to review them in advance — don't let the meeting be the first time you see them.",
    "Special Education Teacher": "Ensure your classroom observation and rating scale data are submitted on time. Late data from any team member can jeopardize the 60-day deadline.",
    "CSE Coordinator / Administrator": "Coordinate the evaluation team early. Getting appointments scheduled, parental consent for outside evaluators, and transportation for assessments all take time.",
    "General Education Teacher": "You will likely be asked to complete behavior rating scales (like Conners or BASC). Complete these promptly and accurately — they significantly influence eligibility decisions.",
}.get(get_role(), "Evaluations must be multidisciplinary — no single test decides eligibility."))

# ── Decision ──────────────────────────────────────────────────────────────────
st.markdown("## 🔀 Decision Point — 60 Days Are Up Tomorrow")
scenario_box("It is now May 27th — one school day before Alex's 60-day deadline. The speech-language evaluation report is not yet complete because the SLP had a scheduling conflict. The eligibility meeting has not been scheduled. What should the CSE do?")
choice = st.radio("What is the correct response?", [
    "A) Hold the eligibility meeting without the SLP report — close enough",
    "B) Request a 30-day extension from the state",
    "C) Acknowledge the violation, notify the parent, complete as quickly as possible, and document what caused the delay",
    "D) Ask the parent to agree to waive the deadline in writing",
], label_visibility="collapsed", key="s4_branch")
if choice:
    if choice.startswith("C"):
        st.success("✅ Correct — there is no official extension process under IDEA. The deadline is missed. The school must acknowledge it, complete the process as urgently as possible, notify the parent, and document the circumstances. The parent may file a state complaint and request compensatory services.")
    elif choice.startswith("A"):
        st.error("❌ Not acceptable. Holding an eligibility meeting without a required evaluation is a procedural violation that could invalidate the eligibility determination.")
    elif choice.startswith("B"):
        st.error("❌ IDEA does not provide for routine 30-day extensions to the 60-day timeline. The deadline is the deadline.")
    else:
        st.error("❌ Parents cannot waive the timeline — it is the school's legal obligation to the child, not just to the parent. A waiver does not absolve the violation.")

st.markdown("---")
st.markdown("## 📝 Knowledge Check")
render_quiz(4, [
    {"q": "Which of the following is NOT a requirement for a valid evaluation?",
     "options": [
         "Must use multiple assessment tools",
         "Must assess all areas of suspected disability",
         "Must be conducted by a licensed medical doctor",
         "Must be conducted by a multidisciplinary team",
     ], "correct": 2,
     "explanation": "Evaluations are conducted by school-based professionals (school psychologist, SLP, OT etc.) — not medical doctors. A medical evaluation may be part of the package but is not always required.",
     "wrong_msg": "Medical doctors are not required for school-based evaluations. The team is made up of certified school professionals."},
    {"q": "What happens if the school misses the 60-day evaluation deadline?",
     "options": [
         "The evaluation is automatically extended 30 more days",
         "The parent forfeits their right to an evaluation",
         "The school is in violation of IDEA and the parent may file a complaint",
         "Nothing — it is just a suggestion",
     ], "correct": 2,
     "explanation": "Missing the 60-day deadline is an IDEA procedural violation. The parent can file a state complaint and may be owed compensatory educational services.",
     "wrong_msg": "The 60-day deadline is a legal requirement, not a suggestion. Violations have real consequences including state investigations and compensatory services."},
    {"q": "A parent disagrees with the school's evaluation results. What is their right?",
     "options": [
         "Nothing — they must accept the school's findings",
         "They can request an Independent Educational Evaluation (IEE) at the school's expense",
         "They can only request a re-read of the same tests",
         "They must wait for the annual review",
     ], "correct": 1,
     "explanation": "If a parent disagrees with the evaluation, they have the right to request an IEE at public expense. The school must either pay for it or file for a due process hearing to defend their evaluation.",
     "wrong_msg": "The IEE right is a strong parent protection. The school cannot simply refuse an IEE request — they must pay for it or immediately initiate a hearing."},
])
