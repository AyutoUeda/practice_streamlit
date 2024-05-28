## Streamlitのデモ

### 起動
```
streamlit run <ファイル名>
```

### 気づいたこと
- ```st.multiselect```の戻り値はlist型
- ```st.markdown```の書き方
```
st.markdown('''
    - a
    - b
''')
```