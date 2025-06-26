# Perplexity Meta Data Extractor
In this repository, you will find the raw Python code I used to transform structured JSON data into readable text-based content in the form of an Excel table.

- 🔗 [GitHub: Perplexity Linked Citations](https://github.com/simodepth96/Perplexity-Meta-Data-Extractor/blob/main/linked_citations.py)
- 🔗 [GitHub: Perplexity Related Queries](https://github.com/simodepth96/Perplexity-Meta-Data-Extractor/blob/main/related_queries.py)


A Streamlit app is also available as a shortcut. Just load your JSON export straight into the app and it'll extract insights in a table-based format.
- 🔗 [Perplexity Meta Data Extractor (Streamlit)](https://perplexity-meta-data-extractor.streamlit.app/)


## ⚠️ Requirements

- **JavaScript Bookmarklet:**
After Perplexity returned an output in response to your prompt, use the following JavScript bookmarklet to export the raw structured data from the conversation.


### Perplexity Grounded Query Extractor

```javascript
javascript:(async()=>{const s=(location.pathname.match(/\/search\/([^/?#]+)/)||[])[1];if(s){const t=Date.now();const q=`with_parent_info=1&with_schematized_response=1&from_first=1&version=2.18&source=default&limit=100&offset=0&supported_block_use_cases=answer_modes&supported_block_use_cases=media_items&supported_block_use_cases=knowledge_cards&supported_block_use_cases=inline_knowledge_cards&_t=${t}`;const r=await fetch(`/rest/thread/${s}?${q}`,{credentials:'include',cache:'no-cache'});if(r.ok){const d=await r.json(),u=URL.createObjectURL(new Blob([JSON.stringify(d,null,2)]));Object.assign(document.createElement('a'),{href:u,download:`perplexity-${s}.json`}).click();setTimeout(()=>URL.revokeObjectURL(u),2e3);}}})();
```


