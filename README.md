# Perplexity Meta Data Extractor
In this repositroy, you will find the raw Python code I used to turn structured JSON data into readable text-based content in the shape of an Excel table.
A Streamlit app is available to dump your JSON file straight away and extract text-based insights.


## ⚠️ Requirements

- **JavaScript Bookmarklet:**
After Perplexity returned an output in response to your prompt, use the following JavScript bookmarklet to export the raw structured data fro mthe conversation.


### Perplexity Grounded Query Extractor

```javascript
javascript:(async()=>{const s=(location.pathname.match(/\/search\/([^/?#]+)/)||[])[1];if(s){const t=Date.now();const q=`with_parent_info=1&with_schematized_response=1&from_first=1&version=2.18&source=default&limit=100&offset=0&supported_block_use_cases=answer_modes&supported_block_use_cases=media_items&supported_block_use_cases=knowledge_cards&supported_block_use_cases=inline_knowledge_cards&_t=${t}`;const r=await fetch(`/rest/thread/${s}?${q}`,{credentials:'include',cache:'no-cache'});if(r.ok){const d=await r.json(),u=URL.createObjectURL(new Blob([JSON.stringify(d,null,2)]));Object.assign(document.createElement('a'),{href:u,download:`perplexity-${s}.json`}).click();setTimeout(()=>URL.revokeObjectURL(u),2e3);}}})();
```

## 🔗 Link to the App 

- [Perplexity Meta Data Extractor (Streamlit)](https://perplexity-meta-data-extractor.streamlit.app/)
- [GitHub: Perplexity Linked Citations](https://github.com/simodepth96/Perplexity-Meta-Data-Extractor/blob/main/linked_citations.py)
- [GitHub: Perplexity Linked Citations](https://github.com/simodepth96/Perplexity-Meta-Data-Extractor/blob/main/linked_citations.py)
