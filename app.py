import numpy as np 
import pandas as pd 
import matplotlib 
import sklearn 
import scipy
import plotly
import streamlit as st

def main():
    st.write(np.__version__)
    st.write(pd.__version__)
    st.write(matplotlib.__version__)
    st.write(sklearn.__version__)
    st.write(scipy.__version__)
    st.write(plotly.__version__)

if __name__ == "__main__":
    main()
