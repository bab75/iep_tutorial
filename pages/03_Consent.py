"""Step 3 — Consent to Evaluate"""
import streamlit as st
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
st.set_page_config(page_title="Step 3 · IEP Tutorial", page_icon="✍️", layout="wide")
from utils.engine import *
apply_theme(); init_session(); sidebar_nav()
page_header("✍️", "Step 3 — Consent to Evaluate", "The 60-day clock starts the moment this form is signed")
step_badge(3)

scenario_box(
    "The school social worker contacts Alex's parents and schedules a Social History Interview "
    "for the following week. At that meeting she explains the evaluation process, what tests will "
    "be used, and asks Alex's mother to sign the consent form. Alex's mother reads it carefully, "
    "asks a few questions, and signs it on March 5th."
)

st.markdown("## What Is Informed Consent?")
info_card("Informed Consent — More Than Just a Signature",
    "Informed consent means the parent fully <b>understands</b> what they are agreeing to. "
    "The school must explain: what evaluations will be conducted, who will conduct them, "
    "what records will be reviewed, and that consent can be withdrawn at any time. "
    "Simply putting a form in front of a parent is NOT informed consent.",
    "#7C3AED")

law_badge("IDEA § 300.300",
    "No evaluation may be conducted without prior written informed consent from the parent. "
    "If the parent refuses, the school may not proceed and cannot override the refusal.")

# ── The 60-day clock ──────────────────────────────────────────────────────────
st.markdown("## ⏱️ The 60-Day Clock")
st.markdown("""
<div style="background:white;border:2px solid #DC2626;border-radius:12px;
            padding:18px 22px;margin:10px 0;">
    <div style="font-family:'Nunito',sans-serif;font-weight:900;color:#DC2626;
                font-size:1.1rem;margin-bottom:8px;">
        From consent signature → IEP meeting: 60 SCHOOL DAYS</div>
    <div style="display:flex;gap:8px;flex-wrap:wrap;margin-bottom:10px;">
        <span style="background:#FEE2E2;color:#7F1D1D;border-radius:20px;
                     padding:3px 12px;font-size:0.78rem;font-weight:700;">
            School days only</span>
        <span style="background:#FEE2E2;color:#7F1D1D;border-radius:20px;
                     padding:3px 12px;font-size:0.78rem;font-weight:700;">
            Excludes weekends + holidays</span>
        <span style="background:#FEE2E2;color:#7F1D1D;border-radius:20px;
                     padding:3px 12px;font-size:0.78rem;font-weight:700;">
            Strict legal deadline</span>
    </div>
    <div style="color:#475569;font-size:0.87rem;line-height:1.75;">
        Within 60 school days the school must: complete ALL evaluations AND hold the 
        IEP meeting where eligibility is determined and (if eligible) the IEP is written.
        Missing this deadline is an IDEA violation regardless of the reason.
    </div>
</div>
""", unsafe_allow_html=True)

# Visual timeline
signed = "March 5"
mid    = "≈ April 14 (30 days)"
late   = "≈ May 8 (50 days)"
dead   = "≈ May 28 (60 days)"
st.markdown(f"""
<div style="background:#F8FAFF;border-radius:10px;padding:16px 20px;margin:10px 0;">
    <div style="font-weight:700;color:#1E293B;font-size:0.85rem;margin-bottom:12px;">
        Alex's 60-Day Timeline (signed {signed})</div>
    <div style="display:flex;align-items:center;gap:0;flex-wrap:nowrap;overflow-x:auto;">
        <div style="background:#2563EB;color:white;border-radius:8px 0 0 8px;
                    padding:10px 14px;min-width:100px;text-align:center;flex-shrink:0;">
            <div style="font-size:0.7rem;opacity:.8;">Signed</div>
            <div style="font-weight:700;font-size:0.82rem;">{signed}</div>
        </div>
        <div style="background:#0D9488;color:white;padding:10px 14px;
                    min-width:120px;text-align:center;flex-shrink:0;">
            <div style="font-size:0.7rem;opacity:.8;">Evals underway</div>
            <div style="font-weight:700;font-size:0.82rem;">{mid}</div>
        </div>
        <div style="background:#D97706;color:white;padding:10px 14px;
                    min-width:120px;text-align:center;flex-shrink:0;">
            <div style="font-size:0.7rem;opacity:.8;">Evals complete</div>
            <div style="font-weight:700;font-size:0.82rem;">{late}</div>
        </div>
        <div style="background:#DC2626;color:white;border-radius:0 8px 8px 0;
                    padding:10px 14px;min-width:120px;text-align:center;flex-shrink:0;">
            <div style="font-size:0.7rem;opacity:.8;">IEP meeting DEADLINE</div>
            <div style="font-weight:700;font-size:0.82rem;">{dead}</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

role_tip({
    "Parent / Caregiver":
        "Note the exact date you sign the consent form. Count 60 school days forward — "
        "that is your legal deadline. If the school has not scheduled a meeting by day 50, "
        "send a written reminder immediately.",
    "Special Education Teacher":
        "Log the consent date in your system the day it is received. Set a calendar "
        "reminder at day 45 to check that all evaluations are complete and the meeting "
        "is scheduled.",
    "CSE Coordinator / Administrator":
        "The 60-day clock has no exceptions for scheduling conflicts or staff shortages. "
        "Plan your caseload to ensure every case can meet its deadline.",
    "General Education Teacher":
        "You may be asked to complete classroom observation data or rating scales as part "
        "of the evaluation. Respond promptly — delays from any team member affect the timeline.",
}.get(get_role(), "The 60-day clock is a strict legal deadline. Log the consent date immediately."))

# ── Decision: parent refuses ──────────────────────────────────────────────────
st.markdown("## 🔀 Decision Point — Parent Refuses to Sign")
scenario_box(
    "At the Social History meeting, Alex's father (who is present) says he does not want "
    "Alex 'labeled' and refuses to sign the consent form. Alex's mother is unsure. "
    "What should the school do?"
)
choice = st.radio("What is the correct response?", [
    "A) Proceed with the evaluation anyway — the teacher's referral is enough",
    "B) Close the case permanently since the parent refused",
    "C) Explain the parent's rights, keep the case open, and document the refusal",
    "D) Call child protective services",
], label_visibility="collapsed", key="s3_branch")
if choice:
    if choice.startswith("C"):
        st.success("✅ Correct! The school must respect the refusal but must keep the case open and continue outreach. The parent can change their mind at any time. The school should explain what evaluation means, address concerns about 'labeling,' and document every contact attempt.")
    elif choice.startswith("A"):
        st.error("❌ Never. Proceeding without parental consent is an IDEA violation regardless of who made the referral. No evaluation can happen without a signed consent form.")
    elif choice.startswith("B"):
        st.error("❌ Not correct. The case must stay open. The parent can sign at any time — even years later. The school should continue periodic outreach and document every attempt.")
    else:
        st.error("❌ Not applicable here. Refusing consent for evaluation is a legal parental right, not a child welfare concern.")

# ── Quiz ──────────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown("## 📝 Knowledge Check")
render_quiz(3, [
    {"q": "Alex's mother signs consent on March 5th. When must the IEP meeting happen by?",
     "options": [
         "March 5th + 60 calendar days = May 4th",
         "March 5th + 60 school days (excluding weekends/holidays)",
         "Within 30 days of the consent",
         "By the end of the school year",
     ], "correct": 1,
     "explanation": "The deadline is 60 SCHOOL DAYS — counting only days school is in session. This is typically about 3 months of actual calendar time.",
     "wrong_msg": "It is 60 school days, not calendar days. Weekends, holidays, and school breaks do not count toward the 60 days."},
    {"q": "What does 'informed consent' require?",
     "options": [
         "Parent reads and signs the form",
         "Parent is fully informed of what will happen, understands it, and voluntarily agrees in writing",
         "Parent agrees verbally at the meeting",
         "Parent signs after one sentence of explanation",
     ], "correct": 1,
     "explanation": "Informed consent requires the parent to understand what they are agreeing to — what tests, who conducts them, what records will be reviewed — before signing.",
     "wrong_msg": "A signature alone is not enough. The parent must genuinely understand what they are consenting to. Informed consent has three parts: information, comprehension, and voluntary agreement."},
    {"q": "A parent partially consents — agrees to the psychological evaluation but not the speech evaluation. What happens?",
     "options": [
         "The school must do all evaluations or none",
         "The school proceeds with only the evaluations the parent consented to",
         "Partial consent invalidates the entire process",
         "The school can override and do all evaluations anyway",
     ], "correct": 1,
     "explanation": "Parents can consent to some evaluations and decline others. The school proceeds with what was consented to and documents the rest.",
     "wrong_msg": "Partial consent is valid. The school conducts the agreed-upon evaluations and must respect the parent's right to decline specific assessments."},
])
