import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def megjelenites():
    st.header("Keresleti függvény")
    st.latex(r"Q_d = a-bP")

    a = st.slider("a – konstans", 40, 200, 100)
    b = st.slider("b – árérzékenység",
                  1.0, 5.0, 2.0, 0.5)
    P = st.slider("P – ár", 0, 100, 20)

    Q = max(0, a - b * P)

    st.latex(rf"Q_d = {a}-{b}\cdot {P}")
    st.metric("Keresett mennyiség", f"{Q:g}")

    arak = np.linspace(0, 110, 500)

    fig, ax = plt.subplots(figsize=(9, 5))

    # Eredeti keresleti görbe
    ax.plot(
        [100 - 2*p for p in np.linspace(0, 50, 200)],
        np.linspace(0, 50, 200),
        "--", color="gray",
        label="Eredeti kereslet"
    )

    # Módosított keresleti görbe
    p_gorbe = np.linspace(0, min(110, a/b), 300)
    q_gorbe = a - b*p_gorbe

    ax.plot(q_gorbe, p_gorbe,
            color="teal", linewidth=3,
            label="Aktuális kereslet")

    if P <= a/b:
        ax.scatter(Q, P, color="orange", s=100)
        ax.plot([0, Q], [P, P], "--", color="orange")
        ax.plot([Q, Q], [0, P], "--", color="orange")

    ax.set_xlim(0, 220)
    ax.set_ylim(0, 110)
    ax.set_xlabel("Mennyiség (Q)")
    ax.set_ylabel("Ár (P)")
    ax.grid(alpha=0.2)
    ax.legend()

    st.pyplot(fig)
    plt.close(fig)
