import streamlit as st
st.title('Math Proof Webpage')
st.write('Welcome to the Math Proof Webpage! This page showcases mathematical proofs.')

st.header('Proof of Pythagoras Theorem')
st.write('The Pythagorean theorem states that in a right-angled triangle, the square of the length of the hypotenuse is equal to the sum of the squares of the lengths of the other two sides.')

st.subheader('Proof:')
st.markdown('''
    We start with a right-angled triangle with sides of lengths a, b, and c (where c is the hypotenuse).
    According to the Pythagorean theorem, we have:

    $$a^2 + b^2 = c^2$$

    Now, let's prove this theorem using geometry:

    [Insert your proof steps here]

    Thus, we have proved the Pythagorean theorem.
''')
