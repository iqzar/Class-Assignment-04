import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Beauty-Full Inventory", layout="centered")
st.sidebar.title("Navigation")

option = st.sidebar.selectbox("Choose a page: ", ["Home", "Inventory", "Sales"])

# Initialize session states
if 'inventory' not in st.session_state:
    st.session_state.inventory = []

if 'sales' not in st.session_state:
    st.session_state.sales = []

# Home Page
if option == 'Home':
    st.title("BEAUTY-FULL")
    st.write("Welcome to your favourite beauty brand")
    st.markdown("""
### 💋 About Us - **BEAUTY-FULL**

At **BEAUTY-FULL**, our mission is to empower individuals to express their true selves through the art of makeup. We believe that beauty has no rules — it's about **confidence, creativity, and feeling good in your own skin**.

Our brand offers a wide range of **high-quality, cruelty-free makeup products** designed to suit every skin tone, type, and style.
""")

# Inventory Page
elif option == 'Inventory':
    st.title("📦 Inventory Stock")

    if st.session_state.inventory:
        st.subheader("Current Inventory")
        inventory_df = pd.DataFrame(st.session_state.inventory)
        st.table(inventory_df)
    else:
        st.info("No products in the inventory yet.")

    st.subheader("➕ Add a New Product to Inventory")
    with st.form("add_inventory_form"):
        product_name = st.text_input("Product Name")
        unit_price = st.number_input("Price per Unit", min_value=0.0, format="%.2f")
        stock_quantity = st.number_input("Available Stock", min_value=0, step=1)
        add_btn = st.form_submit_button("Add Product to Inventory")

        if add_btn:
            if product_name and unit_price >= 0 and stock_quantity >= 0:
                new_product = {
                    "Product Name": product_name,
                    "Price per Unit": unit_price,
                    "Available Stock": stock_quantity
                }
                st.session_state.inventory.append(new_product)
                st.success(f"✅ '{product_name}' added to inventory with {stock_quantity} in stock.")
            else:
                st.error("❗ Please fill in valid product details.")

# Sales Page
elif option == 'Sales':
    st.title("💸 Record a Sale")

    if not st.session_state.inventory:
        st.warning("⚠️ No products available in inventory to sell.")
    else:
        product_names = [p["Product Name"] for p in st.session_state.inventory]

        with st.form("sales_form"):
            selected_product = st.selectbox("Select Product", product_names)
            quantity_sold = st.number_input("Quantity Sold", min_value=1, step=1)
            record_btn = st.form_submit_button("Record Sale")

            if record_btn:
                for product in st.session_state.inventory:
                    if product["Product Name"] == selected_product:
                        if quantity_sold > product["Available Stock"]:
                            st.error("❗ Not enough stock available.")
                        else:
                            product["Available Stock"] -= quantity_sold
                            st.session_state.sales.append({
                                "Product Name": selected_product,
                                "Quantity Sold": quantity_sold
                            })
                            st.success(f"✅ Sale recorded for {quantity_sold} unit(s) of '{selected_product}'")
                        break

        # Display past sales
        if st.session_state.sales:
            st.subheader("📊 Sales History")
            sales_df = pd.DataFrame(st.session_state.sales)
            st.table(sales_df)

            # Aggregate data for chart
            sales_summary = sales_df.groupby("Product Name").sum().reset_index()

            # Bar chart
            st.subheader("📈 Sales Summary Chart")
            fig, ax = plt.subplots()
            ax.bar(sales_summary["Product Name"], sales_summary["Quantity Sold"], color='hotpink')
            ax.set_xlabel("Product")
            ax.set_ylabel("Quantity Sold")
            ax.set_title("Sales by Product")
            st.pyplot(fig)
        else:
            st.info("No sales recorded yet.")
