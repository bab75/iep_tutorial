"""Step 6 — IEP Meeting"""
import streamlit as st, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
st.set_page_config(page_title="Step 6 · IEP Tutorial", page_icon="🤝", layout="wide")
from utils.engine import *
apply_theme(); init_session(); sidebar_nav()
page_header("🤝", "Step 6 — The IEP Meeting", "The team writes Alex's educational plan — you are an equal member")
step_badge(6)

scenario_box("Alex has been found eligible under Specific Learning Disability. The CSE schedules an IEP meeting for May 20th — within the 60-day window. Alex's parents receive written notice at least 5 days in advance. Both parents attend. The team includes the general education teacher, special education teacher, school psychologist, and CSE chairperson.")

info_card("The IEP Meeting", "The IEP meeting is where the team writes the Individualized Education Program — a legally binding document describing goals, services, placement, and accommodations. The parent is a REQUIRED member. The school cannot finalize the IEP without making reasonable efforts to include the parent.", "#16A34A")
law_badge("IDEA § 300.321", "The IEP team must include the parents, a general education teacher, a special education teacher, a district representative, and someone to interpret evaluation results.")

st.markdown("## Required IEP Team Members")
members = [
    ("👨‍👩‍👧", "Parent(s)", "Required. Equal member. Cannot finalize IEP without reasonable efforts to include.", True),
    ("👩‍🏫", "General Education Teacher", "Required if student is/will be in general ed. Informs how to support in class.", True),
    ("👩‍🏫", "Special Education Teacher", "Required. Brings knowledge of specialized instruction.", True),
    ("📋", "District Representative", "Required. Must have authority to commit district resources.", True),
    ("🧠", "Evaluation Interpreter", "Required when evaluations are discussed. Often the school psychologist.", True),
    ("👦", "The Student", "Required when transition is being planned (age 14+). Can attend younger.", False),
    ("🔬", "Related Service Providers", "As appropriate — speech therapist, OT, PT.", False),
]
for icon, name, desc, required in members:
    color = "#16A34A" if required else "#64748B"
    tag = "Required" if required else "As needed"
    st.markdown(f"""
    <div style="display:flex;gap:10px;align-items:flex-start;padding:8px 0;
                border-bottom:1px solid #F1F5F9;">
        <span style="font-size:1.1rem;">{icon}</span>
        <div style="flex:1;">
            <span style="font-weight:700;color:#1E293B;font-size:0.87rem;">{name}</span>
            <span style="background:{'#D1FAE5' if required else '#F1F5F9'};color:{color};
                         border-radius:5px;padding:1px 7px;font-size:0.7rem;
                         font-weight:700;margin-left:6px;">{tag}</span>
            <div style="color:#64748B;font-size:0.82rem;margin-top:2px;">{desc}</div>
        </div>
    </div>""", unsafe_allow_html=True)

role_tip({
    "Parent / Caregiver": "You never have to sign the IEP at the meeting. Take it home and review it. You have the right to ask for clarification on anything. Bring a trusted person with you for support.",
    "Special Education Teacher": "You are responsible for drafting the Present Levels section and annual goals. Have draft goals ready before the meeting but make clear they are drafts — the team writes the IEP together.",
    "CSE Coordinator / Administrator": "Document 3 attempts to contact the parent before holding a meeting without them. A meeting held without the parent when they wanted to attend can be challenged.",
    "General Education Teacher": "Describe specifically how Alex's disability affects his performance in your class. Bring grade data, work samples, and your observations.",
}.get(get_role(), "Parent is a required and equal member of the IEP team."))

st.markdown("## 🔀 Decision Point — Meeting Without Parent")
scenario_box("The IEP meeting is scheduled for May 20th. Alex's father calls the night before to say he cannot attend due to a work emergency. Alex's mother is at a medical appointment. The school has an opening on the calendar and the team is assembled. Should the meeting proceed?")
choice = st.radio("What should happen?", [
    "A) Hold the meeting — the school has done its job by sending notice",
    "B) Hold the meeting and call the parent on speakerphone",
    "C) Reschedule to a time both parents can attend",
    "D) Proceed and send the parents a copy of the completed IEP",
], label_visibility="collapsed", key="s6_branch")
if choice:
    if choice.startswith("C"):
        st.success("✅ Correct! When a parent cannot attend, the school must make a reasonable attempt to reschedule. One call the night before is not sufficient documentation. The meeting should be rescheduled. Only after multiple documented failed attempts may the school proceed without the parent.")
    elif choice.startswith("B"):
        st.warning("⚠️ Partially acceptable — phone participation is allowed and is better than proceeding without any parental input. However, the school should first confirm the parent is willing and able to participate meaningfully by phone before proceeding.")
    else:
        st.error("❌ Not acceptable. The parent is a required team member. A single scheduling conflict does not justify holding the meeting. The school must make reasonable efforts to reschedule.")

st.markdown("---")
st.markdown("## 📝 Knowledge Check")
render_quiz(6, [
    {"q": "Which team member can be excused from an IEP meeting?",
     "options": [
         "The parent — they can be replaced by the school psychologist",
         "A required member if both the parent and school agree in writing",
         "The general education teacher — they are rarely needed",
         "No one — all members must always attend",
     ], "correct": 1,
     "explanation": "Required IEP team members can be excused if both the parent AND the school agree in writing AND the excused member provides written input beforehand.",
     "wrong_msg": "Excusal requires both parties to agree in writing AND the excused member must submit written input. The parent cannot be excused."},
    {"q": "The parent receives the meeting notice the day before. What is the problem?",
     "options": [
         "There is no problem — notice was given",
         "The notice must be given far enough in advance for the parent to attend — typically 5+ school days",
         "The notice must be given 30 days in advance",
         "Only email notice is acceptable",
     ], "correct": 1,
     "explanation": "IDEA requires that meeting notice be given early enough for the parent to have the opportunity to attend. One day's notice is almost never sufficient.",
     "wrong_msg": "Notice must be early enough to give the parent a real opportunity to attend. One day is not enough. Best practice is 5+ school days."},
    {"q": "A parent signs the IEP at the meeting. Can they change their mind?",
     "options": [
         "No — signature is final",
         "Yes — they can revoke consent for services at any time",
         "Only within 24 hours",
         "Only if a new evaluation is done first",
     ], "correct": 1,
     "explanation": "Parents can revoke consent for special education services at any time. The school must stop services when revocation is received.",
     "wrong_msg": "Consent can be revoked at any time. The school must stop services upon receiving the revocation, though they cannot undo what has already been provided."},
])
