import streamlit as  st
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
matplotlib.use('Agg')

def main():

    """
    Common data explorer
    """
    st.title('Common Dataset Explorer ')
    st.subheader('Simple Data explorer ')

    # html_temp = """
    # <div style='background-color:tomato;'><p>Streamlit is Ossum</div>
    # """
    # st.markdown(html_temp,unsafe_allow_html=True)

    def file_selector(folder_path='./datasets/'):
        filenames = os.listdir(folder_path)
        selected_filename = st.selectbox('Select a file',filenames)
        return os.path.join(folder_path,selected_filename)

    filename=file_selector()
    st.info("You Selected {}".format(filename))

    #Read datasets
    df = pd.read_csv(filename)
    #Show datasets
    if st.checkbox('Show Dataset'):
        number = st.number_input("Number of rows to view",5)
        head_tail= st.radio(' Choose Head or Tail',('Head','Tail'))
        if head_tail=='Head':
            st.dataframe(df.head(number))
        if head_tail=='Tail':
            st.dataframe(df.tail(number))


    #Show columns
    if st.checkbox('Column Names'):
        st.write(df.columns)

    #Show Data Types
    # if st.button('Data-types'):
    #     st.text('Data-types')
    #     st.write(df.dtypes)

    #Show Null
    if st.checkbox('Show NUll?'):
        st.write(df.isna().sum())

    #---Drop null--
    if st.button('Drop Null?'):
        df=df.dropna(axis=1)
        st.write(df.shape)
        st.success('Dropped Nan Values')

    # Convert categorical columns to numerical
    if st.checkbox('Show Data-types with columns'):
        st.text('Data-types')
        st.write(df.dtypes)
        all_colss_names=df.columns.tolist()
        sel_cols_names=st.multiselect('Select Categorical Columns to convert into Numerical Columns',all_colss_names,key='cat')
        if st.button("Convert to num data?"):
            df=pd.get_dummies(df,columns=sel_cols_names)
            st.write(df.dtypes)

    #Show Shape
    if st.checkbox("Shape of dataset"):
        # st.write(df.shape)
        data_dim = st.radio('Show dimension by ',('Shape','Rows','Columns'))
        if data_dim == 'Columns':
            st.text('Showing num of cols')
            st.write(df.shape[1])
        elif data_dim == 'Rows':
            st.text('Showing num of rows')
            st.write(df.shape[0])
        elif data_dim == 'Shape':
            st.text('Showing dim')
            st.write(df.shape)

    #Select Columns
    if st.checkbox("Select cols to show"):
        all_cols = df.columns.tolist()
        sel_col = st.multiselect("Select Columns ",all_cols)
        new_df = df[sel_col]
        st.dataframe(new_df)







    # Convert categorical columns to numerical
    # if st.button('Convert categorical to numerical??'):
    #     df1=pd.get_dummies(df)


    #Show Values
    if st.button('Valuecount'):
        st.text('Values By Target/Class')
        st.write(df.iloc[:,-1].value_counts())

    #Show Data Types
    # if st.button('Data-types'):
    #     st.text('Data-types')
    #     st.write(df.dtypes)

    #Show Summary
    if st.checkbox("Summary"):
        st.write(df.describe().T)

    #Info
    # if st.button("Info"):
    #     st.write(df.info())
    #Plot and visualisatons
    # st.subheader('Data visualisatons')
    # #Corr
    # st.subheader('Correlation Plot')
    # c=df.corr()
    # sns.heatmap(c)
    #Seaborn
    if st.checkbox("Correlation Plot Seaborn"):
        st.write(sns.heatmap(df.corr(),annot=True))
        st.pyplot()

    #countPlot
    plt.figure(figsize=(50,50))
    if st.checkbox('Count Plot'):
        st.text('Value counts by target')
        all_cols_names=df.columns.tolist()
        p_col = st.selectbox('Primary Column',all_cols_names)
        sel_col_names=st.multiselect('Select ',all_cols_names)
        if st.button('Plot',key='count'):
            st.text('Generate Plot')
            if sel_col_names:
                vc_plot = df.groupby(p_col[sel_col_names].count())
            else:
                vc_plot = df.iloc[:,-1].value_counts()
            st.write(vc_plot.plot(kind='bar'))
            st.pyplot()
    #pieChart
    if st.checkbox('Pie Plot'):
        all_cols_names = df.columns.tolist()
        sel_col_names = st.multiselect('Select cols to plot',all_cols_names,key='pie')
        if st.button('Generate Plot',key='Pie'):
            st.success('Generating a Pie Plot')
            n=df.iloc[:,-1].value_counts().plot().pie(df[sel_col_names]);
            st.write(n)
            st.pyplot()

    #Customisable plot

    st.subheader('Customisable Plot')
    all_cols_names = df.columns.tolist()
    type_of_plot = st.selectbox('Select Type of Charts',['area','bar','line','hist','box','kde'])
    sel_col_names = st.multiselect('Select cols to plot',all_cols_names)

    if st.button('Generate Plot'):
        st.success('Generating Customisable Plot of {} for {}'.format(type_of_plot,sel_col_names))

        #plot by streamlit
        if type_of_plot=='area':
            cust_data = df[sel_col_names]
            st.area_chart(cust_data)

        elif type_of_plot=='bar':
            cust_data = df[sel_col_names]
            st.bar_chart(cust_data)

        elif type_of_plot=='line':
            cust_data = df[sel_col_names]
            st.line_chart(cust_data)

        elif type_of_plot=='hist':
            cust_plot = df[sel_col_names].plot(kind=type_of_plot)
            st.write(cust_plot)
            st.pyplot()

        elif type_of_plot=='box':
            cust_plot = df[sel_col_names].plot(kind=type_of_plot)
            st.write(cust_plot)
            st.pyplot()

        elif type_of_plot=='kde':
            cust_plot = df[sel_col_names].plot(kind=type_of_plot)
            st.write(cust_plot)
            st.pyplot()















if __name__ == '__main__':
    main()
