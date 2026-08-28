import streamlit as st
import pandas as pd

from database import (
    create_database,
    add_certificate,
    verify_certificate,
    get_all_certificates
)


# ==========================================
# DATABASE
# ==========================================

create_database()


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Certificate Quick Checker",
    page_icon="📜",
    layout="wide"
)


# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

.main-title {
    font-size: 40px;
    font-weight: bold;
    text-align: center;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: gray;
    margin-bottom: 30px;
}

.success-box {
    padding: 20px;
    border-radius: 10px;
    border: 2px solid #28a745;
    margin-top: 20px;
}

.error-box {
    padding: 20px;
    border-radius: 10px;
    border: 2px solid #dc3545;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# TITLE
# ==========================================

st.markdown(
    '<div class="main-title">📜 Certificate Quick Checker</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Quick and easy certificate verification system'
    '</div>',
    unsafe_allow_html=True
)


# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("📋 Menu")

page = st.sidebar.radio(
    "Choose an option",
    [
        "🔍 Verify Certificate",
        "👨‍💼 Admin - Add Certificate",
        "📊 Certificate Database"
    ]
)


# ==========================================
# VERIFY CERTIFICATE
# ==========================================

if page == "🔍 Verify Certificate":

    st.header("🔍 Verify Certificate")

    st.write(
        "Enter the certificate ID to check whether "
        "the certificate is registered in the database."
    )

    certificate_id = st.text_input(
        "Certificate ID",
        placeholder="Example: CERT001"
    )

    if st.button(
        "🔎 Verify Certificate",
        use_container_width=True
    ):

        if certificate_id.strip() == "":

            st.warning(
                "⚠️ Please enter a Certificate ID."
            )

        else:

            result = verify_certificate(
                certificate_id.strip()
            )

            if result:

                st.success("✅ Certificate Verified!")

                st.markdown(
                    '<div class="success-box">',
                    unsafe_allow_html=True
                )

                col1, col2 = st.columns(2)

                with col1:

                    st.write(
                        "**Certificate ID:**",
                        result[0]
                    )

                    st.write(
                        "**Student Name:**",
                        result[1]
                    )

                    st.write(
                        "**Course:**",
                        result[2]
                    )

                with col2:

                    st.write(
                        "**Institution:**",
                        result[3]
                    )

                    st.write(
                        "**Issue Date:**",
                        result[4]
                    )

                    st.write(
                        "**Status:**",
                        result[5]
                    )

                st.markdown(
                    "</div>",
                    unsafe_allow_html=True
                )

            else:

                st.error(
                    "❌ Certificate Not Found"
                )

                st.info(
                    "The entered Certificate ID is not "
                    "registered in our database."
                )


# ==========================================
# ADMIN - ADD CERTIFICATE
# ==========================================

elif page == "👨‍💼 Admin - Add Certificate":

    st.header("👨‍💼 Add New Certificate")

    st.write(
        "Enter certificate details below."
    )

    col1, col2 = st.columns(2)

    with col1:

        certificate_id = st.text_input(
            "Certificate ID",
            placeholder="Example: CERT001"
        )

        student_name = st.text_input(
            "Student Name"
        )

        course = st.text_input(
            "Course"
        )

    with col2:

        institution = st.text_input(
            "Institution"
        )

        issue_date = st.date_input(
            "Issue Date"
        )

    if st.button(
        "➕ Add Certificate",
        use_container_width=True
    ):

        if (
            certificate_id.strip() == ""
            or student_name.strip() == ""
            or course.strip() == ""
            or institution.strip() == ""
        ):

            st.warning(
                "⚠️ Please fill in all fields."
            )

        else:

            success = add_certificate(
                certificate_id.strip(),
                student_name.strip(),
                course.strip(),
                institution.strip(),
                str(issue_date)
            )

            if success:

                st.success(
                    "✅ Certificate added successfully!"
                )

                st.balloons()

            else:

                st.error(
                    "❌ This Certificate ID already exists."
                )


# ==========================================
# DATABASE VIEW
# ==========================================

elif page == "📊 Certificate Database":

    st.header("📊 Certificate Database")

    certificates = get_all_certificates()

    if certificates:

        df = pd.DataFrame(
            certificates,
            columns=[
                "Certificate ID",
                "Student Name",
                "Course",
                "Institution",
                "Issue Date",
                "Status"
            ]
        )

        # Statistics

        total = len(df)

        valid = len(
            df[df["Status"] == "Valid"]
        )

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "📜 Total Certificates",
            total
        )

        col2.metric(
            "✅ Valid Certificates",
            valid
        )

        col3.metric(
            "❌ Invalid Certificates",
            total - valid
        )

        st.divider()

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info(
            "No certificates have been added yet."
        )