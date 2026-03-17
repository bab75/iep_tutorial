"""Step 2 — Referral"""
import streamlit as st
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
st.set_page_config(page_title="Step 2 · IEP Tutorial", page_icon="✉️", layout="wide")
from utils.engine import *
apply_theme(); init_session(); sidebar_nav()
page_header("✉️", "Step 2 — The Referral", "A written referral starts the official clock — here is everything that must happen")
step_badge(2)

scenario_box(
    "Alex's parents, after hearing from Ms. Rivera about their concerns, decide to take action. "
    "Alex's mother writes a letter to the school asking for a full special education evaluation. "
    "She hand-delivers it to the main office on Monday morning and asks the secretary to stamp it "
    "with today's date. The referral process has officially begun."
)

st.markdown("## What is a Referral?")
info_card("The Referral — Starting the Official Process",
    "A <b>referral</b> is the formal request for a special education evaluation. "
    "The moment a written referral is received and date-stamped, the clock starts. "
    "The referral can be made by a parent, teacher, principal, or CSE chairperson. "
    "It does not need special language — a written request asking for an evaluation is sufficient.",
    "#0D9488")

law_badge("IDEA § 300.301",
    "Upon receiving a request for an initial evaluation, the school must "
    "respond with a Prior Written Notice within 5 school days and begin the consent process.")

# ── What happens next ─────────────────────────────────────────────────────────
st.markdown("## What Must Happen After a Referral")
steps_after = [
    ("1", "Date Stamp Immediately", "The school must stamp the referral document with today's date — or the actual date it was received. This date is critical because it starts all timelines.", "#2563EB"),
    ("2", "Send Prior Written Notice (PWN)", "Within 5 school days, the school must send the parent a PWN: Notice of Referral explaining that a referral was received and what will happen next.", "#0D9488"),
    ("3", "Send Procedural Safeguards Notice", "The parent must receive a copy of their full rights (Procedural Safeguards) at this point — their first time in the process.", "#7C3AED"),
    ("4", "Open the Case", "The case is formally opened in the district's system. A social worker or school psychologist is assigned.", "#D97706"),
    ("5", "Schedule Social History Interview", "Within 10 school days, the school social worker must schedule a Social History Interview with the parent.", "#DC2626"),
    ("6", "Begin Consent Process", "The school must begin seeking the parent's informed written consent to evaluate. No testing can happen until consent is signed.", "#16A34A"),
]

for num, title, desc, color in steps_after:
    st.markdown(f"""
    <div style="display:flex;gap:12px;align-items:flex-start;margin-bottom:10px;">
        <div style="background:{color};color:white;border-radius:50%;min-width:28px;
                    height:28px;display:flex;align-items:center;justify-content:center;
                    font-weight:700;font-size:0.85rem;flex-shrink:0;">{num}</div>
        <div style="background:white;border:1px solid #E2E8F0;border-radius:10px;
                    padding:12px 16px;flex:1;">
            <div style="font-weight:700;color:#1E293B;font-size:0.9rem;margin-bottom:3px;">
                {title}</div>
            <div style="color:#475569;font-size:0.84rem;line-height:1.65;">{desc}</div>
        </div>
    </div>""", unsafe_allow_html=True)

# ── Role tips ─────────────────────────────────────────────────────────────────
role_tip({
    "Parent / Caregiver":
        "Always hand-deliver or send your referral by certified mail so you have proof "
        "it was received with a date. Keep a copy for yourself. That date is your legal "
        "starting point for all timelines.",
    "Special Education Teacher":
        "Once a referral is received, you must document it in the district system the "
        "same day. Fax or scan it in. The date on the referral controls all 60-day timelines.",
    "CSE Coordinator / Administrator":
        "Your office must send the PWN within 5 school days — no exceptions. "
        "Log every communication attempt with the parent. This documentation protects "
        "the district if timelines are challenged later.",
    "General Education Teacher":
        "Your written observations and documentation of interventions tried are a key "
        "part of the referral package. Start collecting data now: attendance, grades, "
        "behavior notes, intervention logs.",
}.get(get_role(), "The referral date starts all legal timelines. Keep records from day one."))

# ── Decision branch ───────────────────────────────────────────────────────────
st.markdown("## 🔀 Decision Point — What If the School Delays?")
scenario_box(
    "Alex's mother hand-delivers her written referral on Monday. On Thursday, she calls to "
    "check in and is told 'we haven't had a chance to look at it yet.' By the following "
    "Monday — 5 school days later — she still has not received any written notice from the school."
)

choice = st.radio("What is the correct next step for Alex's mother?", [
    "A) Wait another week — the school is busy",
    "B) Send a follow-up letter in writing asking the school to confirm receipt and date of the referral",
    "C) Withdraw the referral and try again next month",
    "D) Call the teacher — the teacher will handle it",
], label_visibility="collapsed", key="s2_branch")

if choice:
    if choice.startswith("B"):
        st.success("✅ Correct! When the PWN is not received within 5 school days, the parent should follow up IN WRITING — email is fine. This creates a paper trail. If the school continues to delay, this is a procedural violation and a state complaint can be filed.")
    elif choice.startswith("A"):
        st.error("❌ Not correct. The 5-school-day PWN requirement is a legal obligation. Waiting gives the school more time to violate the law. Documenting and following up in writing is the right step.")
    elif choice.startswith("C"):
        st.error("❌ Not correct. Withdrawing the referral lets the school off the hook. The referral date is already established — Alex's mother should press for the school to acknowledge it.")
    else:
        st.error("❌ Not correct. The teacher has limited authority here. The parent should contact the CSE office or principal directly, in writing.")

# ── What if school refuses to accept referral ─────────────────────────────────
st.markdown("## What If the School Refuses to Accept the Referral?")
st.markdown("""
<div style="background:#FEF2F2;border:1px solid #FCA5A5;border-radius:10px;
            padding:14px 18px;margin-bottom:12px;">
    <div style="font-weight:700;color:#DC2626;font-size:0.9rem;margin-bottom:6px;">
        The school cannot legally refuse a referral from a parent.</div>
    <div style="color:#7F1D1D;font-size:0.87rem;line-height:1.75;">
        If the school decides NOT to evaluate, they must send a Prior Written Notice
        explaining why they are refusing — and the parent has the right to challenge that
        decision through mediation or a state complaint.
        <br><br>
        A school that refuses to date-stamp, loses a referral, or claims they never
        received it is committing a Child Find violation. The parent should:<br>
        1. Follow up in writing (email with read receipt)<br>
        2. Keep a copy of the original with the date<br>
        3. Contact the state education department if the school continues to delay
    </div>
</div>
""", unsafe_allow_html=True)

law_badge("IDEA § 300.503",
    "If the school refuses to initiate an evaluation, they must provide Prior Written "
    "Notice stating why — and the parent has full dispute rights.")

# ── Quiz ──────────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown("## 📝 Knowledge Check")
render_quiz(2, [
    {"q": "What must happen within 5 school days of receiving a referral?",
     "options": [
         "The evaluation must begin",
         "The parent must sign consent forms",
         "The school must send the parent a Prior Written Notice",
         "The IEP meeting must be scheduled",
     ], "correct": 2,
     "explanation": "Within 5 school days the school must send a PWN acknowledging the referral. The evaluation cannot begin until the parent signs consent — which comes later.",
     "wrong_msg": "The 5-day requirement is specifically for the Prior Written Notice of Referral. Consent and evaluation come after."},
    {"q": "Alex's mother sends a referral by email on a Tuesday. When does the 60-day clock start?",
     "options": [
         "When the school psychologist reviews it",
         "When the parent signs consent to evaluate",
         "On the Tuesday the email was received",
         "When the IEP team first meets",
     ], "correct": 1,
     "explanation": "The 60-day clock starts when the PARENT SIGNS CONSENT to evaluate — not when the referral is received. The referral just starts the consent process.",
     "wrong_msg": "Important distinction: the referral date starts school obligations (PWN within 5 days), but the 60-day evaluation timeline starts from the consent signature."},
    {"q": "What should a parent always do when submitting a referral?",
     "options": [
         "Submit it verbally so the meeting feels less confrontational",
         "Submit it in writing and keep a copy with the date it was delivered",
         "Ask the teacher to submit it on their behalf",
         "Wait for the school to send a form first",
     ], "correct": 1,
     "explanation": "Written referrals with a documented date create a legal record. Verbal requests are harder to prove and do not start the official timeline reliably.",
     "wrong_msg": "Written documentation is essential. Without a dated copy, it is very difficult to prove timelines were violated if the school delays."},
])
