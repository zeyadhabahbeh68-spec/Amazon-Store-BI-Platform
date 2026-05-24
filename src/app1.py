
# ============================================================
# Amazon Store | Unified Customer & Employee Portal
# Powered by: Zeyad Habahbeh
# ============================================================
import os, csv, datetime
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Amazon Store", page_icon="🛒", layout="wide")

def pick_data_path():
    candidates = [
        "/content/Amazon_Store_Final_Data.csv",
        "/content/amazon.csv",
        "Amazon_Store_Final_Data.csv",
        "amazon.csv",
        "/mnt/data/Amazon_Store_Final_Data.csv",
        "/mnt/data/amazon.csv",
    ]
    for p in candidates:
        if os.path.exists(p):
            return p
    return "/content/Amazon_Store_Final_Data.csv"

DATA_FILE = pick_data_path()
BASE_DIR = os.path.dirname(DATA_FILE) if os.path.dirname(DATA_FILE) else "."
TRANSACTIONS_FILE = os.path.join(BASE_DIR, "amazon_transactions_log.csv")

st.markdown(r'''
<style>
:root{--navy:#131921;--blue:#232f3e;--orange:#ff9900;--ink:#17202a;--muted:#64748b;--line:#e2e8f0;}
html, body, .main, [data-testid="stAppViewContainer"]{
  background: radial-gradient(circle at top left, rgba(255,153,0,.16), transparent 28%), linear-gradient(135deg,#f8fafc 0%,#edf2f7 45%,#f8fafc 100%) !important;
  color:var(--ink); font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Arial,sans-serif;
}
.block-container{padding-top:1rem; padding-bottom:2rem; max-width:1400px;}
[data-testid="stSidebar"]{background:linear-gradient(180deg,var(--navy),var(--blue));}
[data-testid="stSidebar"] *{color:white !important;}
.hero{border-radius:26px;padding:26px 30px;margin-bottom:18px;color:white;background:linear-gradient(120deg,rgba(19,25,33,.98),rgba(35,47,62,.94));box-shadow:0 18px 45px rgba(15,23,42,.20);border:1px solid rgba(255,255,255,.08);}
.hero h1{font-size:42px;margin:0 0 6px 0;color:white;font-weight:900;letter-spacing:.2px;}
.hero p{margin:0;color:#dbe4ee;font-size:15px;}
.powered{display:inline-block;margin-top:12px;background:#ff9900;color:#111827;padding:7px 14px;border-radius:999px;font-weight:900;}
.card{background:rgba(255,255,255,.96);border:1px solid var(--line);border-radius:20px;padding:16px;margin-bottom:12px;box-shadow:0 10px 28px rgba(15,23,42,.08);min-height:210px;}
.card:hover{transform:translateY(-2px);box-shadow:0 16px 36px rgba(15,23,42,.12);transition:.18s ease;}
.product-title{font-size:15px;font-weight:900;line-height:1.25;color:#111827;margin-bottom:10px;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;}
.badge{display:inline-block;padding:4px 10px;border-radius:999px;font-size:12px;font-weight:800;border:1px solid var(--line);background:#fff7ed;color:#9a3412;margin:2px 4px 2px 0;}
.small{font-size:12px;color:var(--muted);}.price{font-size:22px;font-weight:950;color:#b45309;margin-top:6px;}
.kpi-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px;margin:14px 0;}
.kpi{background:rgba(255,255,255,.95);border:1px solid var(--line);border-radius:18px;padding:16px;box-shadow:0 8px 24px rgba(15,23,42,.07);}
.kpi .label{color:var(--muted);font-size:12px;font-weight:700;}.kpi .value{font-size:24px;font-weight:950;color:#111827;margin-top:3px;}
.stButton>button{background:linear-gradient(90deg,#ff9900,#ffb74d);color:#111827;border:0;border-radius:999px;font-weight:900;padding:.45rem 1rem;box-shadow:0 8px 18px rgba(255,153,0,.28);}
.stButton>button:hover{background:linear-gradient(90deg,#ffb74d,#ff9900);transform:translateY(-1px);}
.alert-good{background:#ecfdf5;color:#065f46;border:1px solid #a7f3d0;padding:10px 12px;border-radius:14px;font-weight:800;}
.alert-bad{background:#fff1f2;color:#9f1239;border:1px solid #fecdd3;padding:10px 12px;border-radius:14px;font-weight:800;}
.alert-warn{background:#fffbeb;color:#92400e;border:1px solid #fde68a;padding:10px 12px;border-radius:14px;font-weight:800;}
.footer{text-align:center;color:#64748b;margin-top:24px;font-size:12px;}.report-wrap{background:white;border:1px solid var(--line);border-radius:18px;padding:20px;box-shadow:0 8px 24px rgba(15,23,42,.07);}
@media(max-width:900px){.kpi-grid{grid-template-columns:repeat(2,minmax(0,1fr));}.hero h1{font-size:30px;}}
</style>
''', unsafe_allow_html=True)

def clean_money(s):
    if pd.isna(s): return 0.0
    try: return float(str(s).replace("₹","").replace(",","").replace("%","").strip() or 0)
    except: return 0.0

@st.cache_data(show_spinner=False)
def load_data():
    df = pd.read_csv(DATA_FILE)
    rename = {"product_id":"Product ID","product_name":"Product Name","category":"Category","discounted_price":"Discounted Price (INR)","actual_price":"Actual Price (INR)","discount_percentage":"Discount %","rating":"Rating","rating_count":"Rating Count","about_product":"About Product","product_link":"Product Link","img_link":"Image Link"}
    df = df.rename(columns={c:rename.get(c,c) for c in df.columns})
    if "Product Name" not in df.columns: df["Product Name"] = "Amazon Product"
    if "Category" not in df.columns: df["Category"] = "General"
    if "Discounted Price (INR)" not in df.columns: df["Discounted Price (INR)"] = 0
    if "Actual Price (INR)" not in df.columns: df["Actual Price (INR)"] = df["Discounted Price (INR)"]
    if "Rating" not in df.columns: df["Rating"] = 0
    if "Rating Count" not in df.columns: df["Rating Count"] = 0
    if "Discount %" not in df.columns: df["Discount %"] = 0
    for c in ["Discounted Price (INR)","Actual Price (INR)","Rating","Rating Count","Discount %"]:
        df[c] = df[c].apply(clean_money)
    if "Main Category" not in df.columns: df["Main Category"] = df["Category"].astype(str).str.split("|").str[0].replace("", "General")
    if "Sub Category" not in df.columns: df["Sub Category"] = df["Category"].astype(str).str.split("|").str[1].fillna("General")
    if "Demand Score" not in df.columns:
        df["Demand Score"] = np.log1p(df["Rating Count"].fillna(0)) * (df["Rating"].fillna(0)+1) * 5
    if "Estimated Monthly Demand" not in df.columns:
        mx = max(float(df["Demand Score"].max()),1)
        df["Estimated Monthly Demand"] = np.maximum(10,(df["Demand Score"]/mx*280).round()).astype(int)
    if "Inventory" not in df.columns:
        rng = np.random.default_rng(42)
        df["Inventory"] = np.maximum(15,(df["Estimated Monthly Demand"]*rng.uniform(.35,1.35,len(df))).round()).astype(int)
    if "Reorder Point" not in df.columns: df["Reorder Point"] = np.maximum(10,(df["Estimated Monthly Demand"]*.65).round()).astype(int)
    if "Unit Cost (INR)" not in df.columns: df["Unit Cost (INR)"] = (df["Discounted Price (INR)"]*.68).round(2)
    if "Revenue Potential (INR)" not in df.columns: df["Revenue Potential (INR)"] = (df["Estimated Monthly Demand"]*df["Discounted Price (INR)"]).round(2)
    if "Profit Potential (INR)" not in df.columns: df["Profit Potential (INR)"] = (df["Estimated Monthly Demand"]*(df["Discounted Price (INR)"]-df["Unit Cost (INR)"])).round(2)
    df["Stock Status"] = np.where(df["Inventory"]<df["Reorder Point"],"Below ROP",np.where(df["Inventory"]<1.25*df["Reorder Point"],"Near ROP","Healthy"))
    df = df.reset_index(drop=True); df["Row ID"] = df.index
    return df

def save_data(df):
    df.drop(columns=["Row ID"], errors="ignore").to_csv(DATA_FILE,index=False)
    st.cache_data.clear()

def log_transaction(product, qty, old_inv, new_inv, price):
    header=["Timestamp","Product","Quantity","Unit Price (INR)","Old Inventory","New Inventory","Total Value (INR)"]
    row=[datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), product, int(qty), float(price), int(old_inv), int(new_inv), round(float(qty)*float(price),2)]
    exists=os.path.exists(TRANSACTIONS_FILE) and os.path.getsize(TRANSACTIONS_FILE)>0
    with open(TRANSACTIONS_FILE,"a",newline="",encoding="utf-8") as f:
        w=csv.writer(f)
        if not exists: w.writerow(header)
        w.writerow(row)

def short_name(x,n=82):
    x=str(x); return x if len(x)<=n else x[:n-3]+"..."

def hero(title,subtitle):
    st.markdown(f'<div class="hero"><h1>{title}</h1><p>{subtitle}</p><span class="powered">Powered by: Zeyad Habahbeh</span></div>', unsafe_allow_html=True)

def kpis(items):
    html='<div class="kpi-grid">'
    for label,value in items: html += f'<div class="kpi"><div class="label">{label}</div><div class="value">{value}</div></div>'
    st.markdown(html+'</div>', unsafe_allow_html=True)

df = load_data()
portal = st.sidebar.radio("Choose Portal", ["🛒 Customer Store", "👨‍💼 Employee Dashboard"], index=0)
st.sidebar.markdown("---"); st.sidebar.caption("Amazon Store Analytics System"); st.sidebar.caption("Powered by: Zeyad Habahbeh")

if portal == "🛒 Customer Store":
    hero("Amazon Store", "Fast customer ordering portal with live stock control and professional product cards.")
    c1,c2,c3,c4 = st.columns([1.4,1,1,1])
    with c1: search = st.text_input("Search product", "")
    with c2: cat = st.selectbox("Category", ["All"]+sorted(df["Main Category"].dropna().astype(str).unique().tolist()))
    with c3: sort_by = st.selectbox("Sort by", ["Demand", "Rating", "Price: Low to High", "Price: High to Low"])
    with c4: page = st.number_input("Page", min_value=1, value=1, step=1)
    view = df.copy()
    if search.strip():
        s=search.strip(); view=view[view["Product Name"].astype(str).str.contains(s,case=False,na=False)|view["Category"].astype(str).str.contains(s,case=False,na=False)]
    if cat!="All": view=view[view["Main Category"].astype(str)==cat]
    if sort_by=="Demand": view=view.sort_values("Estimated Monthly Demand",ascending=False)
    elif sort_by=="Rating": view=view.sort_values("Rating",ascending=False)
    elif sort_by=="Price: Low to High": view=view.sort_values("Discounted Price (INR)",ascending=True)
    else: view=view.sort_values("Discounted Price (INR)",ascending=False)
    page_size=24; total_pages=max(1,int(np.ceil(len(view)/page_size))); page=min(int(page),total_pages)
    shown=view.iloc[(page-1)*page_size:page*page_size]
    st.caption(f"Showing {len(shown)} products from {len(view)} results | Page {page} of {total_pages}")
    cols=st.columns(3)
    for i,(_,row) in enumerate(shown.iterrows()):
        with cols[i%3]:
            rid=int(row["Row ID"]); name=row["Product Name"]; price=float(row["Discounted Price (INR)"]); actual=float(row["Actual Price (INR)"]); inv=int(row["Inventory"]); demand=int(row["Estimated Monthly Demand"]); rating=float(row["Rating"])
            st.markdown(f'<div class="card"><div class="product-title">🛍️ {short_name(name)}</div><span class="badge">{row["Main Category"]}</span><span class="badge">⭐ {rating:.1f}</span><div class="price">₹{price:,.0f}</div><div class="small">Actual price: ₹{actual:,.0f} | Inventory: <b>{inv}</b> | Demand: <b>{demand}</b></div></div>', unsafe_allow_html=True)
            qty=st.number_input("Quantity",min_value=0,max_value=999,value=0,step=1,key=f"qty_{rid}")
            if st.button("Confirm Order",key=f"buy_{rid}"):
                if qty<=0: st.markdown("<div class='alert-warn'>Please enter a valid quantity.</div>", unsafe_allow_html=True)
                elif qty>inv: st.markdown(f"<div class='alert-bad'>Insufficient inventory. Available: {inv}</div>", unsafe_allow_html=True)
                else:
                    df2=load_data().copy(); old_inv=int(df2.loc[rid,"Inventory"]); new_inv=old_inv-int(qty)
                    df2.loc[rid,"Inventory"]=new_inv; df2.loc[rid,"Estimated Monthly Demand"]=int(df2.loc[rid,"Estimated Monthly Demand"])+int(qty)
                    save_data(df2); log_transaction(name,qty,old_inv,new_inv,price); st.success(f"Order completed. Remaining inventory: {new_inv}"); st.rerun()
    st.markdown("<div class='footer'>© 2026 Amazon Store | Powered by Zeyad Habahbeh</div>", unsafe_allow_html=True)
else:
    hero("Employee Control Panel", "Inventory, demand analytics, alerts, ABC, EOQ, KPI and executive report.")
    total_products=df["Product Name"].nunique(); total_inv=int(df["Inventory"].sum()); below=int((df["Stock Status"]=="Below ROP").sum()); total_profit=float(df["Profit Potential (INR)"].sum())
    kpis([("Total Products",f"{total_products:,}"),("Total Inventory",f"{total_inv:,}"),("Below ROP",f"{below:,}"),("Profit Potential",f"₹{total_profit:,.0f}")])
    tab1,tab2,tab3,tab4,tab5,tab6,tab7=st.tabs(["📦 Inventory","🔔 Alerts","📈 Analytics","🅰️ ABC","📦 EOQ","📊 KPI","🧾 Report"])
    with tab1:
        st.subheader("📦 Inventory Dashboard")
        c1,c2=st.columns(2)
        with c1: cat_filter=st.selectbox("Filter category",["All"]+sorted(df["Main Category"].astype(str).unique().tolist()),key="invcat")
        with c2: status_filter=st.selectbox("Filter status",["All","Healthy","Near ROP","Below ROP"],key="invstatus")
        v=df.copy()
        if cat_filter!="All": v=v[v["Main Category"]==cat_filter]
        if status_filter!="All": v=v[v["Stock Status"]==status_filter]
        st.dataframe(v[["Product Name","Main Category","Discounted Price (INR)","Rating","Estimated Monthly Demand","Inventory","Reorder Point","Stock Status"]].head(500),use_container_width=True)
    with tab2:
        st.subheader("🔔 Live Stock Alerts")
        below_df=df[df["Stock Status"]=="Below ROP"].sort_values("Demand Score",ascending=False); near_df=df[df["Stock Status"]=="Near ROP"].sort_values("Demand Score",ascending=False)
        if below_df.empty and near_df.empty: st.markdown("<div class='alert-good'>All products are currently healthy.</div>",unsafe_allow_html=True)
        else:
            if not below_df.empty:
                st.markdown(f"<div class='alert-bad'>{len(below_df)} products are below reorder point.</div>",unsafe_allow_html=True); st.dataframe(below_df[["Product Name","Inventory","Reorder Point","Estimated Monthly Demand","Stock Status"]].head(100),use_container_width=True)
            if not near_df.empty:
                st.markdown(f"<div class='alert-warn'>{len(near_df)} products are near reorder point.</div>",unsafe_allow_html=True); st.dataframe(near_df[["Product Name","Inventory","Reorder Point","Estimated Monthly Demand","Stock Status"]].head(100),use_container_width=True)
        if st.button("Auto-Replenish Below ROP Products"):
            df2=load_data().copy(); mask=df2["Inventory"]<df2["Reorder Point"]; df2.loc[mask,"Inventory"]=(df2.loc[mask,"Reorder Point"]*1.4).round().astype(int); save_data(df2); st.success("Replenishment completed."); st.rerun()
    with tab3:
        st.subheader("📈 Product Analytics")
        top=df.sort_values("Estimated Monthly Demand",ascending=False).head(15); fig,ax=plt.subplots(figsize=(10,4)); ax.barh(top["Product Name"].apply(lambda x: short_name(x,35)),top["Estimated Monthly Demand"]); ax.set_xlabel("Estimated Monthly Demand"); ax.set_title("Top 15 Products by Demand"); ax.invert_yaxis(); st.pyplot(fig)
        fig2,ax2=plt.subplots(figsize=(8,4)); ax2.scatter(df["Rating"],df["Rating Count"],alpha=.45); ax2.set_xlabel("Rating"); ax2.set_ylabel("Rating Count"); ax2.set_title("Rating vs Rating Count"); st.pyplot(fig2)
    with tab4:
        st.subheader("🅰️ ABC Analysis")
        abc=df.groupby("Product Name",as_index=False)["Revenue Potential (INR)"].sum().sort_values("Revenue Potential (INR)",ascending=False); total=max(abc["Revenue Potential (INR)"].sum(),1); abc["Cumulative %"]=abc["Revenue Potential (INR)"].cumsum()/total*100; abc["Class"]=np.where(abc["Cumulative %"]<=80,"A",np.where(abc["Cumulative %"]<=95,"B","C")); st.dataframe(abc.head(500),use_container_width=True)
        counts=abc["Class"].value_counts().reindex(["A","B","C"]).fillna(0); fig,ax=plt.subplots(); ax.bar(counts.index,counts.values); ax.set_title("ABC Class Count"); st.pyplot(fig)
    with tab5:
        st.subheader("📦 EOQ Analysis")
        c1,c2=st.columns(2)
        with c1: S=st.number_input("Ordering Cost (S)",1.0,10000.0,500.0,step=50.0)
        with c2: hold_rate=st.number_input("Holding Rate %",1.0,100.0,20.0,step=1.0)/100.0
        eoq=df.copy(); eoq["Annual Demand"]=eoq["Estimated Monthly Demand"]*12; eoq["Holding Cost"]=eoq["Discounted Price (INR)"]*hold_rate; eoq["EOQ"]=np.sqrt((2*eoq["Annual Demand"]*S)/eoq["Holding Cost"].replace(0,np.nan)).fillna(0).round().astype(int); st.dataframe(eoq[["Product Name","Annual Demand","Holding Cost","EOQ","Inventory","Reorder Point"]].sort_values("Annual Demand",ascending=False).head(500),use_container_width=True)
    with tab6:
        st.subheader("📊 KPI Dashboard")
        avg_rating=df["Rating"].mean(); avg_discount=df["Discount %"].mean(); rev=df["Revenue Potential (INR)"].sum(); backorder_risk=(df["Reorder Point"]-df["Inventory"]).clip(lower=0).sum(); kpis([("Average Rating",f"{avg_rating:.2f}"),("Average Discount",f"{avg_discount:.1f}%"),("Revenue Potential",f"₹{rev:,.0f}"),("Backorder Risk Units",f"{int(backorder_risk):,}")])
        category=df.groupby("Main Category",as_index=False).agg({"Revenue Potential (INR)":"sum","Profit Potential (INR)":"sum","Product Name":"count"}).rename(columns={"Product Name":"Products"}).sort_values("Revenue Potential (INR)",ascending=False); st.dataframe(category,use_container_width=True)
    with tab7:
        st.subheader("🧾 Executive Report")
        top5=df.sort_values("Revenue Potential (INR)",ascending=False).head(5)[["Product Name","Main Category","Revenue Potential (INR)","Profit Potential (INR)","Stock Status"]]
        report=f'<div class="report-wrap"><h2>Amazon Store – Executive Summary</h2><p class="small">Powered by: <b>Zeyad Habahbeh</b> | Data file: <b>{os.path.basename(DATA_FILE)}</b></p><hr><b>Total Products:</b> {total_products:,}<br><b>Total Inventory:</b> {total_inv:,}<br><b>Below ROP Products:</b> {below:,}<br><b>Total Profit Potential:</b> ₹{total_profit:,.0f}<br><hr><b>Top Products by Revenue Potential</b>{top5.to_html(index=False)}<hr><p class="small">Use browser print or download as HTML for submission/reporting.</p></div>'
        st.markdown(report,unsafe_allow_html=True); st.download_button("Download Report HTML",report.encode("utf-8"),"Amazon_Store_Report.html","text/html")
    st.markdown("<div class='footer'>© 2026 Amazon Store | Powered by Zeyad Habahbeh</div>",unsafe_allow_html=True)
