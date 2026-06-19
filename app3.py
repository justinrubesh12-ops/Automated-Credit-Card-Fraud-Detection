import streamlit as st
import base64
import pandas as pd
import plotly.express as px
import joblib as jb


st.set_page_config(page_title="Tree and boosting analytics on fraud", layout="wide")


def apply_custom_theme():
    try:
        with open("bg4.png", "rb") as img:
            encoded = base64.b64encode(img.read()).decode()
    except:
        encoded = ""

    st.markdown(f"""
        <style>
        /* Main App Background Setup */
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-attachment: fixed;
        }}
        
        /* JET-BLACK SIDEBAR WITH NEON RED BORDER & GLOW */
        [data-testid="stSidebar"], [data-testid="stSidebar"] > div:first-child {{
            background-color: #000000 !important;
            background: #000000 !important;
            border-right: 2px solid #ff0000 !important;
            box-shadow: 0 0 20px #ff0000 !important;
        }}

        /* Force all native Streamlit sidebar text elements to stay readable (White) */
        [data-testid="stSidebar"] *, [data-testid="stSidebar"] p, [data-testid="stSidebar"] label {{
            color: #ffffff !important;
        }}

        /* PROFILE CONTAINER BOX WITH MATCHING GLOW */
        .profile-card {{
            background-color: #000000 !important;
            border: 2px solid #ff0000 !important;
            border-radius: 15px !important;
            padding: 20px !important;
            text-align: center !important;
            box-shadow: 0 0 15px #ff0000, 0 0 30px rgba(255, 0, 0, 0.4) !important;
            margin-bottom: 20px !important;
        }}

        /* FIXED: CRITICAL FIXED CSS FOR EXPLICIT GLOWING ROUNDED IMAGE */
        .neon-avatar {{
            width: 160px;
            height: 160px;
            border-radius: 50% !important;
            border: 3px solid #ff0000 !important;
            box-shadow: 0 0 15px #ff0000, 0 0 30px rgba(255, 0, 0, 0.6) !important;
            object-fit: cover;
            margin: 0 auto 15px auto;
            display: block;
        }}

        /* NEON TYPOGRAPHY INSIDE SIDEBAR */
        .profile-name {{
            color: #ffffff !important;
            font-size: 24px !important;
            font-weight: bold !important;
            text-shadow: 0 0 8px #ff0000, 0 0 15px #ff0000 !important;
            margin-top: 15px !important;
            margin-bottom: 5px !important;
        }}

        .profile-role {{
            color: #ff9999 !important;
            font-size: 16px !important;
            text-shadow: 0 0 5px rgba(255, 0, 0, 0.5) !important;
            margin-bottom: 15px !important;
        }}
        
        /* Specific Glowing Title and Header Elements matching the letters style */
        .glowing-title {{ 
            color: #ffffff !important; 
            text-shadow: 0 0 10px #ff0000, 0 0 20px #ff0000, 0 0 30px #ff0000 !important; 
            font-weight: bold; 
            font-size: 3em; 
        }}
        
        .glowing-creator {{ 
            color: #ffffff !important; 
            text-shadow: 0 0 8px #ff0000, 0 0 15px #ff0000 !important; 
            font-weight: bold; 
            font-size: 1.5em; 
            text-align: center;
        }}
        
        /* Global Headers Sync */
        h1, h2, h3, h4, h5, h6 {{ 
            color: #ffffff !important; 
            text-shadow: 0 0 12px #ff0000, 0 0 25px #ff0000 !important; 
        }}
        
        /* MAIN CONTENT GLOWING CONTAINERS */
        .custom-box {{
            background-color: #000000 !important;
            border: 2px solid #ff0000 !important;
            border-radius: 10px !important;
            padding: 20px !important;
            box-shadow: 0 0 15px #ff0000, 0 0 25px rgba(255,0,0,0.4) !important;
            margin-bottom: 25px !important;
        }}
        
        /* Native Streamlit Dataframes styling matching the black/red grid */
        [data-testid="stDataFrame"], [data-testid="stDataEditor"], .js-plotly-plot {{
            background-color: #000000 !important;
            border: 2px solid #ff0000 !important;
            border-radius: 10px !important;
            box-shadow: 0 0 15px #ff0000 !important;
        }}
        </style>
    """, unsafe_allow_html=True)


apply_custom_theme()


def get_image_base64(path):
    try:
        with open(path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode()
    except Exception as e:
        return ""

with st.sidebar:
    st.markdown('''<div class="profile-card">
                PROFILE DETAIL''', unsafe_allow_html=True)

   
    img_filename = "WhatsApp Image 2026-06-18 at 9.42.44 AM.jpeg"
    img_b64 = get_image_base64(img_filename)
    
    if img_b64:
        st.markdown(f'<img src="data:image/jpeg;base64,{img_b64}" class="neon-avatar">', unsafe_allow_html=True)
    else:
        st.error("Profile Image Missing")

    st.markdown(
        """
        <p class="profile-name">Justin R Nadar</p>
        <p class="profile-role">AI & AIML Engineer</p>
        """,
        unsafe_allow_html=True
    )
    

    st.markdown("""
### Education :=
B.Tech CSE (AI & AIML)

### Skills :=
- Machine Learning
- Deep Learning
- Python
- Streamlit
- Data Analytics
- Data Visualization

### Projects :=
- Attrition Prediction System
- ML Analytics Dashboard
- Fraud Detection System
- Family Algorithm Comparison

### Connect :=
GitHub: https://github.com/justinrubesh12-ops

LinkedIn: https://www.linkedin.com/in/justin-raju-nadar-7616a3355/

Email: justinrubesh12@gmail.com
""")

    st.markdown('</div>', unsafe_allow_html=True)


def apply_neon_chart(fig):
    fig.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    return fig



if "page" not in st.session_state: 
    st.session_state.page = "home"


if st.session_state.page != "home":
    if st.button("🏠 RETURN TO HOME"):
        st.session_state.page = "home"
        st.rerun()


if st.session_state.page == "home":
    st.markdown("<h1 style='text-align:center;' class='glowing-title'>Automated Credit Card Fraud Detection & Transaction Amount Prediction System</h1>", unsafe_allow_html=True)
    st.markdown('<p class="glowing-creator">creator : JUSTIN R NADAR</p>', unsafe_allow_html=True)
    st.divider()

    if st.button("VIEW STORY"):
        st.session_state.page = "SMALL_STORY"
        st.rerun()

elif st.session_state.page == "SMALL_STORY":
    st.header("DEVELOPMENT STORY")
    st.divider()
    st.subheader("1. Introduction to the Project")
    st.markdown("""
Financial institutions process thousands of transactions every second.

Fraudulent transactions can lead to significant financial losses and security risks. Detecting these transactions accurately and efficiently is therefore essential.

This project implements an automated Machine Learning pipeline capable of:
- Detecting fraudulent transactions
- Predicting transaction amounts
- Comparing multiple ensemble algorithms
- Automatically selecting the best-performing models

The system combines model optimization, evaluation, and deployment-ready outputs to create a complete end-to-end ML solution.
""")
    st.divider()
    
    st.subheader("2. Problem Statement and Objectives")
    st.markdown("""
Traditional fraud detection systems often rely on fixed rules that struggle to identify new and evolving fraud patterns.

At the same time, financial institutions require accurate transaction analysis to better understand customer behavior and manage financial risks.

The primary objectives of this project are:
- Detect fraudulent transactions with high accuracy.
- Predict transaction amounts using machine learning.
- Compare multiple ensemble learning algorithms.
- Perform automated hyperparameter optimization.
- Select the best-performing classification and regression models.
- Create deployment-ready models for real-time predictions.

This project aims to build a complete automated machine learning workflow that improves both fraud detection and transaction analysis.
""")
    st.divider()
    
    st.subheader("3. Dataset Understanding and Preparation")
    st.markdown("""
The project uses a credit card transaction dataset containing various transaction-related features, transaction amounts, and fraud labels.

Before model training, the dataset was carefully prepared to ensure reliable and accurate predictions.

Key preprocessing steps included:
- Loading and inspecting the dataset.
- Identifying numerical and categorical features.
- Separating target variables for classification and regression tasks.
- Creating feature and target datasets.
- Splitting the data into training and testing sets.
- Preparing the dataset for machine learning model training.

For this project:
- **Classification Target:** Class (Fraud / Non-Fraud)
- **Regression Target:** Amount (Transaction Value)

Proper data preparation ensures that the machine learning models can learn meaningful patterns and generalize effectively to unseen transactions.
""")
    st.divider()
    
    st.subheader("4. Automated Machine Learning Pipeline")
    st.markdown("""
To eliminate manual model selection and improve efficiency, an automated machine learning pipeline was developed.

The system automatically trains, evaluates, and compares multiple ensemble learning algorithms for both classification and regression tasks.

The pipeline includes:
- Multiple ensemble machine learning models.
- Automated hyperparameter optimization.
- Performance evaluation using appropriate metrics.
- Best model selection based on results.
- Automated result storage for future analysis.

Regression Algorithms Used:
- Random Forest Regressor | Extra Trees Regressor | Gradient Boosting Regressor
- AdaBoost Regressor | LightGBM Regressor | CatBoost Regressor

Classification Algorithms Used:
- Random Forest Classifier | Extra Trees Classifier | Gradient Boosting Classifier
- AdaBoost Classifier | LightGBM Classifier | CatBoost Classifier

This automated approach reduces manual effort and creates a scalable workflow for machine learning experimentation and deployment.
""")
    st.divider()
    
    st.subheader("5. Model Training and Hyperparameter Optimization")
    st.markdown("""
Multiple ensemble learning models were trained using the prepared dataset.

To improve performance, RandomizedSearchCV was used to automatically explore different hyperparameter combinations and identify the optimal settings for each model.

This process helps improve model accuracy, reduces manual tuning efforts, and ensures the selection of the most effective model configuration.
""")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("GO TO RESULTS"):
            st.session_state.page = "result"
            st.rerun()
    with col2:
        if st.button("RETURN TO HOME"):
            st.session_state.page = "home"
            st.rerun()

elif st.session_state.page == "result":
    choice = st.selectbox("SELECT TYPE", ["REGRESSION", "CLASSIFICATION"])
    if choice == "CLASSIFICATION":
        st.header("CLASSIFICATION RESULTS OVERVIEW")
        try:
            opt = st.selectbox("Select View", ["comparison data fram", "best model dataframe"])
            
            if opt == "comparison data fram":
                df = pd.read_csv("classification_rsult.csv")
                st.markdown('''
    <div class="custom-box">
        <h3 style="margin-top: 0;">BEST CLASSIFICATION MODEL</h3>
        <p>I chose this classification model based on a comparison of six different models. The final selection was determined by the following metrics:</p>
        <ul>
            <li>1. ACCURACY</li>
            <li>2. PRECISION</li>
            <li>3. RECALL</li>
            <li>4. F1 SCORE</li>
        </ul>
    </div>
''', unsafe_allow_html=True)
            else:
                df = pd.read_csv("best_classification_rslt.csv")
                st.markdown('''
    <div class="custom-box">
        <h3 style="margin-top: 0;">BEST CLASSIFICATION MODEL</h3>
        <p>This dataframe shows you the final winner. This result is chosen based on the F1-score because when data imbalance occurs, standard accuracy metrics can give misleading results.</p>
        <ul>
            <li><strong>FINAL SCORE DRIVEN BY:</strong> F1 SCORE</li>
        </ul>
    </div>
''', unsafe_allow_html=True)
            st.dataframe(df, use_container_width=True)
        except: 
            st.error("Files not found.")
        
    else:
        st.header("REGRESSION RESULTS OVERVIEW")
        try:
            opt = st.selectbox("Select View", ["comparison data fram", "best model dataframe"])
            if opt == "comparison data fram":
                df = pd.read_csv("regression_result.csv") 
                st.markdown('''
    <div class="custom-box">
        <h3 style="margin-top: 0;">REGRESSOR COMPARISON MATRIX</h3>
        <p>I evaluated these models based on a comprehensive validation suite across four explicit metric boundaries:</p>
        <ul>
            <li>1. MAE (Mean Absolute Error)</li>
            <li>2. MSE (Mean Squared Error)</li>
            <li>3. RMSE (Root Mean Squared Error)</li>
            <li>4. R2 SCORE</li>
        </ul>
    </div>
''', unsafe_allow_html=True)
            else:
                df = pd.read_csv("best_regressor.csv")
                st.markdown('''
    <div class="custom-box">
        <h3 style="margin-top: 0;">BEST REGRESSION MODEL WINNER</h3>
        <p>The optimal architecture configuration was cleanly chosen from the model variations.</p>
        <ul>
            <li><strong>CRITICAL SORT KEY:</strong> R2 SCORE</li>
        </ul>
    </div>
''', unsafe_allow_html=True)
            st.dataframe(df, use_container_width=True)
        except: 
            st.error("Files not found.")

    if st.button("VIEW ANALYTICS"):
        st.session_state.page = "chart"
        st.rerun()

elif st.session_state.page == "chart":
    st.header("VISUAL ANALYTICS OF REGRESSION AND CLASSIFICATION")
    try:
        main_option = st.selectbox("SELECT THE FAMILY", ["REGRESSION", "CLASSIFICATION"])
        if main_option == "CLASSIFICATION":
            clas_df = pd.read_csv("classification_rsult.csv")
            options = st.selectbox("Select Chart", ["Bar Chart", "Scatter Chart", "Line Chart", "Heatmap"])
        
            if options == "Bar Chart": 
                fig = px.bar(clas_df, x="score", y="model", title="Accuracy based bar chart :=")
                st.markdown('''
        <div class="custom-box">
            <h3 style="margin-top: 0;">BAR CHART REPORT :=</h3>
            <p>Plotting 'Model' against 'Accuracy' creates an intuitive layout to rapidly inspect competitive trade-offs between algorithmic boundaries.</p>
        </div>
    ''', unsafe_allow_html=True)
               
            elif options == "Scatter Chart": 
                fig = px.scatter(clas_df, x="precision", y="recall")
                st.markdown('''
        <div class="custom-box">
            <h3 style="margin-top: 0;">SCATTER CHART REPORT :=</h3>
            <p>Visualizing the true Precision-Recall trade-off space across evaluated algorithms.</p>
        </div>''', unsafe_allow_html=True)
                
            elif options == "Line Chart": 
                fig = px.line(clas_df, x="model", y=["score","precision", "recall", "f1"])
                st.markdown('''
        <div class="custom-box">
            <h3 style="margin-top: 0;">LINE CHART REPORT :=</h3>
            <p>Multi-Metric performance variance plotted sequentially over evaluation iterations.</p>
        </div>''', unsafe_allow_html=True)

            else: 
                fig = px.imshow(clas_df.set_index("model")[["score", "precision", "recall", "f1"]], text_auto=True)
                st.markdown('''
        <div class="custom-box">
            <h3 style="margin-top: 0;">HEATMAP REPORT :=</h3>
            <p>Color-coded performance evaluation grid allowing rapid auditing of algorithmic scores.</p>
        </div>''', unsafe_allow_html=True)
            st.plotly_chart(apply_neon_chart(fig), use_container_width=True)
            
        else:
            reg_df = pd.read_csv("regression_result.csv")
            options = st.selectbox("Select Chart", ["Bar Chart", "Scatter Chart", "Line Chart", "Heatmap"])
            
            if options == "Bar Chart": 
                fig2 = px.bar(reg_df, x="mae", y="model", title="r2 based bar chart :=")
                st.markdown('''
        <div class="custom-box">
            <h3 style="margin-top: 0;">BAR CHART REPORT :=</h3>
            <p>Comparing Mean Absolute Error metrics. Lower tracking metrics indicate precise prediction accuracy.</p>
        </div>''', unsafe_allow_html=True)
                
            elif options == "Scatter Chart": 
                fig2 = px.scatter(reg_df, x="mse", y="rmse")
                st.markdown('''
        <div class="custom-box">
            <h3 style="margin-top: 0;">SCATTER CHART REPORT :=</h3>
            <p>Evaluating covariance trends between Mean Squared Error and Root Mean Squared Error metrics.</p>
        </div>''', unsafe_allow_html=True)

            elif options == "Line Chart": 
                fig2 = px.line(reg_df, x="model", y=["mae","mse", "rmse", "r2"])
                st.markdown('''
        <div class="custom-box">
            <h3 style="margin-top: 0;">LINE CHART REPORT :=</h3>
            <p>Simultaneous performance boundary comparison across multiple validation criteria dimensions.</p>
        </div>''', unsafe_allow_html=True) 
            else: 
                fig2 = px.imshow(reg_df.set_index("model")[["mae","mse", "rmse", "r2"]], text_auto=True)
                st.markdown('''
        <div class="custom-box">
            <h3 style="margin-top: 0;">HEATMAP REPORT :=</h3>
            <p>Consolidated error matrices providing quick visibility into algorithmic architecture evaluation scores.</p>
        </div>''', unsafe_allow_html=True)
                
            st.plotly_chart(apply_neon_chart(fig2), use_container_width=True)
            
    except: 
        st.error("Data missing.")
    col1,col2=st.columns(2)
    with col1:
        if st.button("live prediction"):
            st.session_state.page="live"
            st.rerun()
    with col2:
        if st.button("return home"):
             st.session_state.page="home"
             st.rerun()

elif st.session_state.page=="live":
    st.header("Live prediction")
    st.divider()
    model=jb.load("best_classifier.pkl")
    model2=jb.load("best_regressor.pkl")
    feature=jb.load("feature.pkl")
    choice2=st.selectbox("select family",["REGRESSOR","CLASSIFIER"])
    if choice2 == "CLASSIFIER":
        user_input={}
        for ke,val in feature.items():
            user_input[ke] = st.number_input(
        label=ke,
        min_value=float(val["min"]),
        max_value=float(val["max"]),
        value=float(val["mean"])
    )
            
        input_df=pd.DataFrame([user_input])
        st.write("Feature Count:", len(feature))
        st.write("Input Shape:", input_df.shape)
        prediction=model.predict(input_df)
        st.subheader("employee report :=")
        st.write(input_df)
        prob = model.predict_proba(input_df)
        st.write(
            f"Fraud Probability: {prob[0][1]*100:.2f}%"
        )
        if prediction[0]==1:
            st.error("THIS NEWS IS FRAUD")
        else:
            st.success("THIS IS ORIGINAL")
    else:
       
        user_input = {}

        for k,v in feature.items():
            user_input[k] = st.number_input(
                label=k,
                min_value=float(v["min"]),
                max_value=float(v["max"]),
                value=float(v["mean"])
            )

        input_df = pd.DataFrame([user_input])

        pred = model2.predict(input_df)

        st.subheader("Prediction Report")
        st.write(input_df)

        st.metric(
            label="Predicted Value",
            value=f"{pred[0]:.4f}"
        )
        actual_amount = st.number_input(
        "Enter Actual Transaction Amount",
        min_value=0.0,
        value=0.0
       )
        difference = abs(actual_amount - pred[0])

        st.metric(
            label="Difference",
            value=f"{difference:.4f}"
        )

        # Anomaly Check
        if pred[0] > 0:
            percentage_difference = (
                difference / pred[0]
            ) * 100

            if percentage_difference > 50:
                st.warning("⚠️ Unusual Transaction")
            else:
                st.success("✅ Usual Transaction")


# st.write("Feature Count:", len(feature))
# st.write("Input Shape:", input_df.shape)
# st.write(input_df.head())
# st.write(input_df.columns.tolist())
# st.write(model2.feature_names_in_)