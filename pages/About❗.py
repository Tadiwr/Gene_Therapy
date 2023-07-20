import streamlit as st

st.write("# What is the purpose of this predictor?")

"""
Gene therapy is the process of inserting a gene with the correct
gene sequence inorder to fix genetic disorders

It is possible that one could be be born or inherit genes that are incorrect and this can result in 
genetic disorders like sickle cell anemia.

Gene therapies dont have a high overall success rate according to this extract from Nature Media.


    In a first report, the industry lobby group BIO, 
    along with analysts at BioMedTracker and Amplion,
    analysed 7,455 drug development programmes that 
    moved through the clinic between 2006 and 2015. 
    They found that the probability of success was 
    63% in Phase I trials, 31% in Phase II trials, 
    58% in Phase III trials and 85% during the 
    regulatory review process, for an **overall 
    success rate of 9.6% (63% × 31% × 58% × 85% = 9.6%).**



Link to full article: [Nature Media Research](https://www.nature.com/articles/nrd.2016.136#:~:text=They%20found%20that%20the%20probability,%C3%97%2085%25%20%3D%209.6%25)

```python
👨‍🔬🟰 (63% × 31% × 58% × 85% = 9.6%).
```

It is worth mentioning that this is the overall success of gene therapy trials by averaging the success rate in 
different theurapitic areas where gene therapy has been used

# What we decided to do?
We then decided to use machine leanring to build a model that can predict the efficacy(in short success)
of the trial before conducting the actual trial

So doctors and scientists can

- play around with different variables and see which ones are important to the success of the trial
- avoid the expensive costs of running gene therapy trials that were most likely going to fail (e.g. human loss and finacial costs)
- overrally imporove the efficacy of these gene therapy trials

"""



