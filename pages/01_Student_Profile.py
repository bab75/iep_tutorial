"""Step 1 — Meet the Student"""
import streamlit as st
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
st.set_page_config(page_title="Step 1 · IEP Tutorial", page_icon="👦", layout="wide")
from utils.engine import *
apply_theme(); init_session(); sidebar_nav()
page_header("👦", "Step 1 — Meet the Student", "Learn how a student enters the IEP process through Child Find")
step_badge(1)

rc = get_role_config()

scenario_box(
    "Alex is 8 years old and in 2nd grade. His teacher, Ms. Rivera, has noticed that "
    "Alex struggles to read even simple words, frequently loses his place on the page, "
    "and avoids writing tasks. Despite extra help in class, he is falling further behind "
    "his peers. His parents have also noticed he avoids reading at home and gets frustrated "
    "quickly. The school has tried some general education interventions but Alex is still "
    "struggling after 10 weeks."
)

# ── Child Find ────────────────────────────────────────────────────────────────
st.markdown("## What is Child Find?")
info_card("Child Find — Federal IDEA Requirement",
    "Every school district in the United States has a legal obligation called "
    "<b>Child Find</b> — to actively identify, locate, and evaluate every child "
    "who may have a disability and need special education services. This includes "
    "children in public schools, private schools, homeless children, and children "
    "not yet enrolled in school.",
    "#2563EB")

law_badge("IDEA § 300.111",
    "Child Find applies to all children from birth through age 21, including those "
    "who are advancing from grade to grade but may still need special education.")

role_tip({
    "Parent / Caregiver":
        "You have the right to refer your own child for evaluation at any time. "
        "You do not need to wait for the school to bring it up first.",
    "Special Education Teacher":
        "Any professional DOE staff member who suspects a disability has an obligation "
        "to bring this to the principal or CSE chairperson — not to ignore it.",
    "CSE Coordinator / Administrator":
        "Child Find is a proactive obligation. 'We waited to see if they improved' "
        "is not an acceptable defense for delayed identification.",
    "General Education Teacher":
        "Ms. Rivera's observations are critical. General ed teachers are often the "
        "first to notice a student may need evaluation. Document what you see.",
}.get(get_role(), "Child Find is the school's obligation to identify students who may need special education."))

# ── Who can trigger ───────────────────────────────────────────────────────────
st.markdown("## Who Can Start the Process?")
c1, c2 = st.columns(2)
with c1:
    for who, desc, color in [
        ("👨‍👩‍👧 Parent or Guardian", "Can request evaluation in writing at any time. No reason required beyond suspecting a disability.", "#2563EB"),
        ("👩‍🏫 Teacher or School Staff", "Professional staff who suspect a disability can request a referral to the principal or CSE.", "#0D9488"),
        ("🏫 School Principal", "Can initiate a referral when a disability is suspected.", "#7C3AED"),
    ]:
        st.markdown(f"""
        <div style="background:white;border-left:4px solid {color};border-radius:8px;
                    padding:12px 14px;margin-bottom:8px;">
            <div style="font-weight:700;color:{color};font-size:0.88rem;">{who}</div>
            <div style="color:#475569;font-size:0.83rem;margin-top:3px;">{desc}</div>
        </div>""", unsafe_allow_html=True)
with c2:
    for who, desc, color in [
        ("📋 CSE Chairperson", "Can initiate referrals for students not attending DOE schools.", "#D97706"),
        ("🏥 Outside Agency", "Certain agencies (early intervention, courts) can request referrals.", "#DC2626"),
        ("🚫 What is NOT required", "Parent does NOT need a diagnosis. Teacher does NOT need proof. Suspicion alone is enough to trigger the process.", "#16A34A"),
    ]:
        st.markdown(f"""
        <div style="background:white;border-left:4px solid {color};border-radius:8px;
                    padding:12px 14px;margin-bottom:8px;">
            <div style="font-weight:700;color:{color};font-size:0.88rem;">{who}</div>
            <div style="color:#475569;font-size:0.83rem;margin-top:3px;">{desc}</div>
        </div>""", unsafe_allow_html=True)

# ── Decision branch ───────────────────────────────────────────────────────────
st.markdown("## 🔀 Decision Point")
st.markdown("""
<div style="background:#FFF8E1;border:2px solid #D97706;border-radius:12px;
            padding:16px 20px;margin:10px 0;">
    <div style="font-weight:700;color:#D97706;font-size:0.9rem;margin-bottom:8px;">
        Scenario: Ms. Rivera tells the principal about Alex's struggles.
        The principal says "Let's wait another month and see how he does."
        What should happen?
    </div>
</div>
""", unsafe_allow_html=True)

choice = st.radio("What is the correct response?", [
    "A) Wait the month as the principal suggests — more data is better",
    "B) Ms. Rivera should document her concerns in writing and push for a referral",
    "C) The parent must complain first before anything can happen",
    "D) Only a psychologist can decide if a referral is needed",
], label_visibility="collapsed", key="s1_branch")

if choice:
    if choice.startswith("B"):
        st.success("✅ Correct! Child Find is a proactive obligation. Waiting to refer when a disability is suspected is itself a potential IDEA violation. Ms. Rivera should document her concerns in writing and refer to the CSE. The parent can also be informed of their right to request an evaluation independently.")
    elif choice.startswith("A"):
        st.error("❌ Not quite. 'Wait and see' is one of the most common Child Find violations. Once a disability is reasonably suspected, the school must act — not delay. Delaying can cost the student valuable intervention time.")
    elif choice.startswith("C"):
        st.error("❌ Not correct. Parents have rights but the school does not need parent permission to make a referral for evaluation. The Child Find obligation is the school's responsibility, not dependent on parent complaint.")
    else:
        st.error("❌ Not correct. No single person controls whether a referral happens. Any professional staff member, the principal, or the parent can trigger the referral process.")

# ── Key facts ─────────────────────────────────────────────────────────────────
st.markdown("## Key Facts for Step 1")
facts = [
    ("Child Find is proactive", "Schools must actively look for students who may need services — not wait for parents to ask."),
    ("No diagnosis needed", "A disability does not need to be diagnosed by a doctor before a referral can be made. Suspicion is enough."),
    ("Anyone can refer", "Parent, teacher, principal, or CSE chairperson. Written request is best — keeps a record with a date."),
    ("General Ed interventions run parallel", "RTI/MTSS support is fine — but it cannot be used to delay the referral process if a disability is suspected."),
    ("All children are covered", "Public school students, private school students, homeless students, students advancing grade to grade."),
]
for title, desc in facts:
    st.markdown(f"""
    <div style="display:flex;gap:10px;padding:8px 0;border-bottom:1px solid #F1F5F9;
                align-items:flex-start;">
        <span style="color:#2563EB;font-size:1rem;flex-shrink:0;margin-top:2px;">▸</span>
        <div><span style="font-weight:700;color:#1E293B;font-size:0.87rem;">{title}:</span>
             <span style="color:#475569;font-size:0.87rem;"> {desc}</span></div>
    </div>""", unsafe_allow_html=True)

# ── Quiz ──────────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown("## 📝 Knowledge Check")
render_quiz(1, [
    {"q": "What is Child Find?",
     "options": [
         "A parent's right to request services",
         "The school district's legal obligation to identify all children who may have disabilities",
         "A federal database of students with IEPs",
         "A voluntary program for struggling students"
     ], "correct": 1,
     "explanation": "Child Find is the school district's proactive legal duty under IDEA to identify, locate, and evaluate ALL children with disabilities — whether or not they have been referred.",
     "wrong_msg": "Child Find is the school's obligation — not just a parent right. It is a proactive legal duty under IDEA § 300.111."},
    {"q": "Alex's teacher suspects he has a learning disability. What is the FIRST step?",
     "options": [
         "Wait for Alex's parents to contact the school",
         "Have Alex repeat 2nd grade first",
         "Document concerns and bring them to the principal or CSE for a referral",
         "Refer Alex to the school counselor only"
     ], "correct": 2,
     "explanation": "When a school professional suspects a disability, they must bring this forward for a referral. Waiting or rerouting to counseling only delays the process.",
     "wrong_msg": "The teacher has an independent obligation to flag a suspected disability. Waiting for parents or trying other alternatives first can be a Child Find violation."},
    {"q": "Which students does Child Find cover?",
     "options": [
         "Only students enrolled in public schools",
         "Only students whose parents have requested evaluation",
         "All children including private school students, homeless students, and those advancing grade to grade",
         "Only students with a medical diagnosis of a disability"
     ], "correct": 2,
     "explanation": "Child Find covers ALL children — in public schools, private schools, homeless, and even those passing their classes but suspected of having a disability.",
     "wrong_msg": "Child Find is broader than most people realize — it covers all children regardless of school type, housing status, or whether they are passing their classes."},
])
