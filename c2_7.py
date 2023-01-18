st=input("Enter a string:")
if st.endswith('ing'):
    st += 'ly'
elif len(st) >= 3:
    st += 'ing'
print(st)    
