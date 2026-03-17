"""Step 8 — Consent & Mandates"""
import streamlit as st, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
st.set_page_config(page_title="Step 8 · IEP Tutorial", page_icon="📋", layout="wide")
from utils.engine import *
apply_theme(); init_session(); sidebar_nav()
page_header("📋", "Step 8 — Consent & Mandates", "The IEP is agreed to — now services must actually begin")
step_badge(8)

scenario_box("The IEP is complete. Alex will receive: Resource Room 5x/week for reading and writing, Speech-Language Therapy 2x/week, and extended time on all tests. The school sends the IEP home with Alex's parents. They read it carefully over the weekend and sign consent for services on May 25th. Alex's mandated services must now begin.")

info_card("IEP Consent vs Evaluation Consent — Two Different Things",
    "There are <b>two separate consent forms</b> in the IEP process. "
    "(1) Consent to EVALUATE — given before assessments. "
    "(2) Consent for SERVICES — given after the IEP is written. "
    "A parent who consented to evaluate has NOT automatically agreed to the IEP. "
    "A parent can agree to some services and refuse others.",
    "#9333EA")
law_badge("IDEA § 300.300(b)", "Parental consent must be obtained before providing special education and related services for the first time.")

st.markdown("## What Are Mandates?")
st.markdown("""
<div style="background:#EFF6FF;border-left:4px solid #2563EB;border-radius:8px;padding:14px 18px;margin:10px 0;">
    <div style="font-weight:700;color:#1E40AF;margin-bottom:6px;">Mandates = What the IEP legally requires the school to provide</div>
    <div style="color:#334155;font-size:0.88rem;line-height:1.75;">
        Once an IEP is agreed to, the services listed in it are <b>mandated</b> — legally binding obligations on the school.
        If the school fails to provide any mandated service, this is an IDEA violation. 
        The parent can file a complaint and request compensatory services for every missed session.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("## Alex's Mandates")
mandates = [
    ("Resource Room", "5x per week", "40 min each session", "Special Education Teacher", "Must begin within 30 days of IEP"),
    ("Speech-Language Therapy", "2x per week", "30 min each session", "Licensed SLP", "Must begin within 30 days of IEP"),
    ("Extended Time", "All tests and assignments", "1.5x standard time", "All teachers", "Effective immediately upon IEP implementation"),
]
for service, freq, dur, provider, timing in mandates:
    st.markdown(f"""
    <div style="background:white;border:1px solid #E2E8F0;border-radius:10px;
                padding:12px 16px;margin-bottom:8px;display:flex;gap:12px;flex-wrap:wrap;">
        <div style="min-width:160px;"><div style="font-weight:700;color:#1E293B;font-size:0.88rem;">{service}</div>
        <div style="color:#64748B;font-size:0.78rem;margin-top:2px;">{provider}</div></div>
        <div style="flex:1;display:flex;gap:10px;flex-wrap:wrap;">
            <span style="background:#DBEAFE;color:#1E40AF;border-radius:6px;padding:3px 10px;font-size:0.78rem;">{freq}</span>
            <span style="background:#D1FAE5;color:#065F46;border-radius:6px;padding:3px 10px;font-size:0.78rem;">{dur}</span>
            <span style="background:#FEF3C7;color:#92400E;border-radius:6px;padding:3px 10px;font-size:0.78rem;">{timing}</span>
        </div>
    </div>""", unsafe_allow_html=True)

role_tip({
    "Parent / Caregiver": "Keep a session log. Note when services happen and when they are cancelled. If sessions are being missed regularly, document it in writing and contact the school. Missed sessions are compensable.",
    "Special Education Teacher": "Services must be logged. Every session provided — or missed — should be documented. If you cannot provide a session, reschedule it. Cancelled sessions are not automatically forgiven.",
    "CSE Coordinator / Administrator": "Implementation of the IEP is a legal obligation from day one. Ensure that all providers have received the IEP and understand their responsibilities before services are due to begin.",
    "General Education Teacher": "Accommodations listed in the IEP (extended time, read-aloud, etc.) apply in your class starting immediately. You must implement them for every applicable assignment and test.",
}.get(get_role(), "Mandated services are legally binding. Missed sessions must be made up."))

st.markdown("## 🔀 Decision Point — Parent Refuses the IEP")
scenario_box("After reviewing the IEP, Alex's father says he does not want Alex pulled out of class for Resource Room — he thinks it will embarrass Alex. He refuses to sign consent for services. What happens?")
choice = st.radio("What is the consequence?", [
    "A) The school can begin services anyway — the IEP team agreed",
    "B) Services cannot begin. The school issues a PWN and the parent can take more time to decide",
    "C) Alex loses his eligibility permanently",
    "D) The school must hold a new IEP meeting immediately",
], label_visibility="collapsed", key="s8_branch")
if choice:
    if choice.startswith("B"):
        st.success("✅ Correct! Without consent, no services can begin. The school issues a Prior Written Notice and the case stays open. The parent can change their mind at any time. The school should address the parent's specific concerns — in this case, concerns about stigma — and explain the ICT option or in-class push-in models.")
    elif choice.startswith("A"):
        st.error("❌ Never. Services absolutely cannot begin without parental consent. This would be a direct IDEA violation.")
    elif choice.startswith("C"):
        st.error("❌ Not correct. Refusing services does not revoke eligibility. Alex remains eligible. The parent can consent to services at any time.")
    else:
        st.error("❌ Not required immediately. The school must issue a PWN documenting the refusal and keep the case open. A new meeting may be helpful if concerns can be addressed, but it is not mandatory.")

st.markdown("---")
st.markdown("## 📝 Knowledge Check")
render_quiz(8, [
    {"q": "Alex's parents signed consent to evaluate in March. Do they need to sign again for services?",
     "options": [
         "No — one signature covers everything",
         "Yes — consent for services is a separate form",
         "Only if the services are more than 2 hours per week",
         "Only if the parent was not at the IEP meeting",
     ], "correct": 1,
     "explanation": "Consent to evaluate and consent for services are two entirely separate documents. Signing one does not authorize the other.",
     "wrong_msg": "There are two distinct consent forms. The parent must sign both — one before evaluation and one before services begin."},
    {"q": "Alex's Resource Room sessions are being cancelled regularly due to teacher absence. What should his parents do?",
     "options": [
         "Accept it — cancellations happen sometimes",
         "Document the cancellations and request in writing that sessions be rescheduled as compensatory services",
         "Immediately file for due process",
         "Contact the teacher directly",
     ], "correct": 1,
     "explanation": "Regular cancellations without make-up sessions are an IEP violation. Parents should document every missed session and request compensatory services in writing.",
     "wrong_msg": "Missed sessions are not acceptable without make-up time. Documenting and requesting compensation in writing is the right first step before escalating to a complaint."},
    {"q": "What does it mean when services are 'mandated' in an IEP?",
     "options": [
         "The school will try to provide them when convenient",
         "The services are legally required to be provided as written",
         "The parent must pay for them",
         "They are suggestions from the evaluation team",
     ], "correct": 1,
     "explanation": "Mandated services are legal obligations. The IEP is a legally binding document. If the school fails to provide what is written, they are violating IDEA.",
     "wrong_msg": "IEP services are not suggestions — they are legal mandates. Failure to provide them is an IDEA violation with real consequences."},
])
