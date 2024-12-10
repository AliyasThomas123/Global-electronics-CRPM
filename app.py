import streamlit as st
import pandas as pd
from services.entity_service import EntityService
from repository.customer_repository import CustomerRepository
from repository.product_repository import ProductRepository
from repository.purchase_repository import PurchaseRepository
from services.analytics_service import AnalyticsService
from models.customer import Customer
from models.product import Product
from models.purchase import Purchase
from datetime import datetime
import matplotlib.pyplot as plt
import altair as alt

# Page Configuration
st.set_page_config(page_title="CRPM System", layout="wide")
def search_dynamic_table(data , columns,search_term):
    if data:
            df = pd.DataFrame(data, columns=columns)
            
            filtered_df = df[
                df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)
            ] if search_term else df
            return filtered_df




st.markdown("""
    <style>        
 .glow-img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 50%;
        box-shadow: 0 0 15px red, 0 0 30px red, 0 0 45px red;
        border-radius: 10px;
    }
          </style>
            """
            ,unsafe_allow_html=True)

with st.sidebar:
    image_path = "https://img.freepik.com/free-vector/customers-laptop-headset-giving-thumb-up-rating-stars-customer-feedback-customer-rating-feedback-customer-relationship-management-concept_335657-773.jpg?t=st=1733037179~exp=1733040779~hmac=4e8a902a865c0155d045efb5269dd50b56029f23c9e11b934ad07975ba1133b3&w=996"
    st.markdown(f'<img src="{image_path}" style="width:100%; height:auto;" class ="glow-img">'
                ,unsafe_allow_html=True)

# Sidebar for Navigation
st.sidebar.title("Global Electronics")
st.sidebar.text("know your Customers!")
menu_option = st.sidebar.radio(
    "Navigate to:", ["Customer Management", "Product Management", "Purchase Management", "Dashboard"]
)

# ------ Customer Management ------
if menu_option == "Customer Management":
    st.title("Customer Management")
    tabs = st.tabs(["Add Customer", "View Customers", "Deactivate Customer"])

    # Tab: Add Customer
    with tabs[0]:
        st.header("Add a New Customer")
        with st.form(key="add_customer_form"):
            name = st.text_input("Customer Name", key="name")
            email = st.text_input("Email Address", key="email")
            phone = st.text_input("Phone Number", key="phone")
            submit_button = st.form_submit_button("Add Customer")
            if submit_button:
                cust_obj = Customer(1,name,email,phone,is_active=True)
                res = EntityService.add_entity(
                   cust_obj
                )
                st.success(res)

    # Tab: View Customers
    with tabs[1]:
        st.header("View All Customers")
        customers = CustomerRepository.get_all_customers()
        if customers:
            search_term = st.text_input("Search Customer")
            filtered_df = search_dynamic_table(customers , ["ID", "Name", "Email", "Phone", "Active"],search_term)
            st.table(filtered_df)
        else:
            st.info("No customers available.")

    # Tab: Deactivate Customer
    with tabs[2]:
        st.header("Deactivate a Customer")
        customers = CustomerRepository.get_all_customers()
        if customers:
                search_term = st.text_input("Search Customr")
                filtered_df = search_dynamic_table(customers , ["ID", "Name", "Email", "Phone", "Active"],search_term)
                st.table(filtered_df)
                selected_id = st.selectbox("Select Customer ID to Deactivate", filtered_df["ID"])
                if st.button("Deactivate Customer"):
                        CustomerRepository.deactivate_customer(selected_id)
                        st.success(f"Customer ID {selected_id} deactivated successfully!")
        else:
            st.info("No customers to deactivate.")

# ------ Product Management ------
elif menu_option == "Product Management":
    st.title("Product Management")
    tabs = st.tabs(["Add Product", "View Products", "Deactivate Product" , "Update Stock"])

    # Tab: Add Product
    with tabs[0]:
        st.header("Add a New Product")
        with st.form(key="add_product_form"):
            name = st.text_input("Product Name")
            price = st.number_input("Price", min_value=0.0)
            stock = st.number_input("Stock Quantity", min_value=0)
            submit_button = st.form_submit_button("Add Product")
            if submit_button:
                prod_obj = Product(1 , name,price,stock)
                res=EntityService.add_entity(prod_obj)
                if res:
                    st.success(res)
            

    # Tab: View Products
    with tabs[1]:
        st.header("View All Products")
        products = ProductRepository.get_all_products()
        if products:
            search_term = st.text_input("Search Products")
            filtered_df = search_dynamic_table(products , ["ID", "Name", "Price", "Quantity", "Active"],search_term)
            st.table(filtered_df)
        else:
            st.info("No products available.")

    # Tab: Deactivate Product
    with tabs[2]:
        st.header("Deactivate a Product")
        products = ProductRepository.get_all_products()
        if products:
            search_term = st.text_input("Search Product")
            filtered_pdc_df = search_dynamic_table(products , ["ID", "Name", "Price", "Quantity", "Active"],search_term)
            st.table(filtered_pdc_df)
            selected_id = st.selectbox("Select Product ID to Deactivate", filtered_pdc_df["ID"])
            if st.button("Deactivate Product"):
                ProductRepository.deactivate_product(selected_id)
                st.success(f"Product ID {selected_id} deactivated successfully!")
        else:
            st.info("No products to deactivate.")
    

    with tabs[3]:
        st.header("Update Stock")
        products = ProductRepository.get_all_products()
        if products:
            search_term = st.text_input("Search Item")
            filtered_pdc_df = search_dynamic_table(products , ["ID", "Name", "Price", "Quantity", "Active"],search_term)
            st.table(filtered_pdc_df)
            selected_id = st.selectbox("Select Product ID to Update Stock", filtered_pdc_df["ID"])
            quantity = st.text_input("Enter Quantity")
            if st.button("Update Product"):
                ProductRepository.stock_update(selected_id , quantity)
                st.success(f"Product ID {selected_id} Updated successfully!")
        else:
            st.info("No products to deactivate.")

# ------ Purchase Management ------
elif menu_option == "Purchase Management":
    st.title("Purchase Management")
    tabs = st.tabs(["Record Purchase", "View Purchase History"])

    # Tab: Record Purchase
    with tabs[0]:
        col1, col2 = st.columns(2)

        with col1:
            st.header("Customers")
            customers = CustomerRepository.get_all_customers()
            if customers:
                search_term = st.text_input("Search Customr")
                filtered_df = search_dynamic_table(customers , ["ID", "Name", "Email", "Phone", "Active"],search_term)
                st.table(filtered_df)
            else:
                st.info("No customers Available")
            

        with col2:
            st.header("Products")
            products = ProductRepository.get_all_products()
            if products:
                search_term = st.text_input("Search Product")
                filtered_pdc_df = search_dynamic_table(products , ["ID", "Name", "Price", "Quantity", "Active"],search_term)
                st.table(filtered_pdc_df)
            else:
                st.info("No Products Available")
        st.markdown("<div class='centered-form'>", unsafe_allow_html=True)
        st.header("Record Purchase")
        with st.form(key="purchase_form"):
           
            customer = st.selectbox("Select Customer", filtered_df['ID'])

            product = st.selectbox("Select Product",  filtered_pdc_df['Name'])
            p_id =list(filtered_pdc_df[filtered_pdc_df['Name'] == product]['ID'].to_dict().values())
            print("ID",p_id)

            quantity = st.number_input("Quantity", min_value=1)
            price=list( filtered_pdc_df[filtered_pdc_df['Name'] == product]['Price'].to_dict().values())
            print("price",price[0])
            total = int(quantity) * float(price[0])
            submit = st.form_submit_button("Record Purchase")
            day =datetime.now().strftime("%Y-%m-%d")
            if submit:
                pur_obj = Purchase(1,customer,p_id[0],quantity,total,date=day)
                #print(pur_obj)
                res=EntityService.add_entity(pur_obj)
                print(res)
                st.success(f"Purchase recorded successfully !")
        st.markdown("</div>", unsafe_allow_html=True)
    # Tab: View Purchase History
    with tabs[1]:
        st.header("View Purchase History")
        
        purchases = PurchaseRepository.get_all_purchases()
        if purchases:
                st.table(pd.DataFrame(purchases , columns=['customer_id','CustomerName','product_id','ProductName','quantity','purchase_id']))
        else:
                st.info("No purchase history for this customer.")

# ------ Dashboard ------
elif menu_option == "Dashboard":
    st.title("Dashboard")
    tabs = st.tabs(["Sales Overview", "Top Customers", "Product Performance"])

    # Tab: Sales Overview
    with tabs[0]:
        st.header("Sales Overview")
        sales_report = AnalyticsService.generate_report("sales")
        if sales_report:
            st.table(pd.DataFrame(sales_report,columns=['ProductNamae' , 'TotalSales','Profit']))
        else:
            st.info("No sales data available.")

    # Tab: Top Customers
    with tabs[1]:
        st.header("Top Customers")
        top_customers = AnalyticsService.generate_report("top_customers")
        if top_customers:
            st.table(pd.DataFrame(top_customers,columns=['customer_id','total_purchases']))
        else:
            st.info("No data available for top customers.")

    # Tab: Product Performance
    with tabs[2]:
        st.header("Product Performance")
        product_performance = AnalyticsService.generate_report("sales")
        if product_performance:
            df= pd.DataFrame(product_performance,columns=['ProductNamae' , 'TotalSales','Profit'])
           
            new = df[['ProductNamae' , 'Profit']]
            # Create the line chart using Altair
            chart = alt.Chart(new).mark_line(point=True).encode(
                x="ProductNamae:N",  # Product Name as a nominal (categorical) field
                y="Profit:Q",        # Profit as a quantitative field
                tooltip=["ProductNamae", "Profit"]
            ).properties(
                title="Profit by Product"
            )

            # Render the Altair chart in Streamlit
            st.altair_chart(chart, use_container_width=True)


        else:
            st.info("No data available for product performance.")
