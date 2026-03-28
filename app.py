import streamlit as st
from urllib.parse import quote

st.set_page_config(
    page_title="Uni Application Assistant",
    page_icon="🎓",
    layout="centered",
)

WHATSAPP_NUMBER = "256726322079"
WHATSAPP_MESSAGE = (
    "Hello Uni Application Assistant, I want help applying to university. "
    "I am ready to share my university choices, course choices, and my A-Level/O-Level results."
)
WHATSAPP_LINK = f"https://wa.me/{WHATSAPP_NUMBER}?text={quote(WHATSAPP_MESSAGE)}"


def app_css():
    st.markdown(
        """
        <style>
        :root {
            --bg: #081c15;
            --bg-soft: #0f2a22;
            --card: rgba(255, 255, 255, 0.06);
            --card-strong: rgba(255, 255, 255, 0.09);
            --text: #f5fff8;
            --muted: #cfe7d6;
            --accent: #52b788;
            --accent-2: #95d5b2;
            --line: rgba(255,255,255,0.10);
            --warning: #ffe8a3;
        }

        .stApp {
            background:
                radial-gradient(circle at top right, rgba(82,183,136,0.18), transparent 28%),
                radial-gradient(circle at top left, rgba(149,213,178,0.12), transparent 22%),
                linear-gradient(180deg, #061710 0%, #081c15 45%, #0b2219 100%);
            color: var(--text);
        }

        .block-container {
            padding-top: 1.2rem;
            padding-bottom: 3rem;
            max-width: 760px;
        }

        h1, h2, h3, h4, p, li, div, span {
            color: var(--text);
        }

        .hero {
            padding: 1.35rem 1.1rem 1.2rem 1.1rem;
            border: 1px solid var(--line);
            border-radius: 24px;
            background: linear-gradient(180deg, rgba(255,255,255,0.08), rgba(255,255,255,0.03));
            box-shadow: 0 18px 50px rgba(0,0,0,0.22);
            margin-bottom: 1rem;
        }

        .eyebrow {
            display: inline-block;
            padding: 0.35rem 0.7rem;
            border-radius: 999px;
            background: rgba(82,183,136,0.18);
            color: #dff8e8;
            font-size: 0.82rem;
            font-weight: 700;
            letter-spacing: 0.02em;
            margin-bottom: 0.8rem;
        }

        .hero h1 {
            font-size: 2rem;
            line-height: 1.1;
            margin: 0 0 0.7rem 0;
        }

        .hero p {
            font-size: 1rem;
            line-height: 1.55;
            color: var(--muted);
            margin-bottom: 0.8rem;
        }

        .price-box {
            margin-top: 1rem;
            padding: 0.95rem 1rem;
            border-radius: 18px;
            background: rgba(82,183,136,0.13);
            border: 1px solid rgba(149,213,178,0.20);
        }

        .price-title {
            font-size: 0.9rem;
            color: var(--accent-2);
            font-weight: 700;
            margin-bottom: 0.2rem;
        }

        .price-amount {
            font-size: 1.75rem;
            font-weight: 800;
            margin-bottom: 0.25rem;
        }

        .price-note {
            color: var(--muted);
            font-size: 0.95rem;
            line-height: 1.45;
        }

        .grid-2 {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 0.9rem;
            margin: 1rem 0;
        }

        .info-card, .step-card, .req-card, .disclaimer-card {
            border: 1px solid var(--line);
            border-radius: 20px;
            background: var(--card);
            padding: 1rem;
        }

        .info-card h3,
        .step-card h3,
        .req-card h3,
        .disclaimer-card h3 {
            margin-top: 0;
            margin-bottom: 0.5rem;
            font-size: 1.06rem;
        }

        .muted {
            color: var(--muted);
        }

        .step-number {
            width: 34px;
            height: 34px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            border-radius: 999px;
            background: rgba(82,183,136,0.18);
            color: white;
            font-weight: 800;
            margin-bottom: 0.55rem;
        }

        .req-list {
            margin: 0;
            padding-left: 1.1rem;
        }

        .req-list li {
            margin-bottom: 0.65rem;
            color: var(--muted);
            line-height: 1.45;
        }

        .cta-wrap {
            margin-top: 1rem;
            padding: 1rem;
            border-radius: 22px;
            background: linear-gradient(180deg, rgba(82,183,136,0.16), rgba(255,255,255,0.04));
            border: 1px solid rgba(149,213,178,0.22);
            text-align: center;
        }

        .cta-title {
            font-size: 1.2rem;
            font-weight: 800;
            margin-bottom: 0.45rem;
        }

        .cta-sub {
            color: var(--muted);
            margin-bottom: 0.9rem;
            line-height: 1.5;
        }

        .cta-button {
            display: inline-block;
            width: 100%;
            text-align: center;
            padding: 0.95rem 1rem;
            border-radius: 16px;
            text-decoration: none;
            font-weight: 800;
            font-size: 1rem;
            color: #062d1d !important;
            background: linear-gradient(180deg, #95d5b2, #52b788);
            box-shadow: 0 10px 24px rgba(0,0,0,0.18);
        }

        .cta-button:hover {
            filter: brightness(1.03);
        }

        .mini-note {
            margin-top: 0.8rem;
            font-size: 0.88rem;
            color: var(--muted);
            line-height: 1.45;
        }

        .disclaimer-card {
            margin-top: 1rem;
            background: rgba(255,255,255,0.045);
        }

        .footer-note {
            margin-top: 1rem;
            text-align: center;
            font-size: 0.86rem;
            color: var(--muted);
            opacity: 0.95;
        }

        @media (max-width: 700px) {
            .hero h1 {
                font-size: 1.7rem;
            }

            .grid-2 {
                grid-template-columns: 1fr;
            }

            .block-container {
                padding-top: 0.8rem;
                padding-left: 0.9rem;
                padding-right: 0.9rem;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def main():
    app_css()

    st.markdown(
        """
        <section class="hero">
            <div class="eyebrow">Fast university application support</div>
            <h1>Uni Application Assistant</h1>
            <p>
                We help students apply to their preferred universities without the stress of figuring out the whole portal process alone.
                You simply send us your academic details on WhatsApp, we handle the application work for you, and we complete it fast.
            </p>

            <div class="price-box">
                <div class="price-title">Simple flat fee</div>
                <div class="price-amount">UGX 14,000</div>
                <div class="price-note">
                    Covers application support for <strong>up to 3 universities</strong>.<br>
                    Whether you apply to 1, 2, or 3 universities, the fee remains the same.
                </div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="grid-2">
            <div class="info-card">
                <h3>What we do</h3>
                <p class="muted">
                    We guide and handle the application entry process for students who already know the universities and courses they want.
                    Our goal is to make the process quick, simple, and less stressful.
                </p>
            </div>

            <div class="info-card">
                <h3>How fast?</h3>
                <p class="muted">
                    Once you send the needed information clearly on WhatsApp, we aim to complete your application in about
                    <strong>20 minutes</strong>.
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("## What you need before you message us")

    st.markdown(
        """
        <div class="req-card">
            <ul class="req-list">
                <li><strong>Your university choices</strong> — up to 3 universities you want to apply to.</li>
                <li><strong>At least 4 course choices</strong> you are interested in applying for.</li>
                <li><strong>Your A-Level results.</strong></li>
                <li><strong>Your O-Level results.</strong></li>
            </ul>
            <p class="muted" style="margin-top:0.8rem;">
                Other details like your phone number, email address, district, and similar personal information
                will be requested directly in the WhatsApp chat during the application process.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("## How it works")

    st.markdown(
        """
        <div class="grid-2">
            <div class="step-card">
                <div class="step-number">1</div>
                <h3>Open WhatsApp</h3>
                <p class="muted">
                    Tap the button below to start a chat with us instantly.
                </p>
            </div>

            <div class="step-card">
                <div class="step-number">2</div>
                <h3>Send your requirements</h3>
                <p class="muted">
                    Share your university choices, course choices, A-Level results, and O-Level results.
                </p>
            </div>

            <div class="step-card">
                <div class="step-number">3</div>
                <h3>We handle the application</h3>
                <p class="muted">
                    We continue with the remaining details in chat and complete the portal application for you.
                </p>
            </div>

            <div class="step-card">
                <div class="step-number">4</div>
                <h3>Done in about 20 minutes</h3>
                <p class="muted">
                    Our process is designed to be fast, clear, and student-friendly.
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="cta-wrap">
            <div class="cta-title">Ready to apply?</div>
            <div class="cta-sub">
                Start the WhatsApp chat now and send us your application details.
            </div>
            <a class="cta-button" href="{WHATSAPP_LINK}" target="_blank">
                Chat with us on WhatsApp
            </a>
            <div class="mini-note">
                Tapping the button opens WhatsApp with a ready-made message so the conversation starts quickly.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="disclaimer-card">
            <h3>Disclaimer</h3>
            <p class="muted">
                Uni Application Assistant is <strong>not affiliated with any university</strong>.
                We are an independent student-led support service that helps applicants complete university applications
                to their preferred institutions.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="footer-note">
            Uni Application Assistant • Student-led university application support
        </div>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
