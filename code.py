import streamlit as st
import pandas as pd
import json
from io import BytesIO
import traceback

def extract_web_results(data):
    """Extract web results from Perplexity JSON data"""
    try:
        web_results = (
            data['entries'][0]['blocks'][1]['plan_block']['steps'][2]['web_results_content']['web_results']
        )
        
        # Flatten into a list of dictionaries
        rows = []
        for result in web_results:
            rows.append({
                "Title": result.get("name", ""),
                "URL": result.get("url", ""),
                "Snippet": result.get("snippet", ""),
                "Domain": result.get("meta_data", {}).get("domain_name", ""),
                "Published Date": result.get("meta_data", {}).get("published_date", "")
            })
        
        return pd.DataFrame(rows)
    
    except (KeyError, IndexError, TypeError) as e:
        st.error(f"Could not extract web results. Error: {e}")
        return pd.DataFrame()

def extract_related_queries(data):
    """Extract related queries from Perplexity JSON data"""
    try:
        related_queries = data['entries'][0].get('related_queries', [])
        
        # Convert to DataFrame
        if related_queries:
            df_queries = pd.DataFrame(related_queries, columns=["Related Queries"])
        else:
            df_queries = pd.DataFrame(columns=["Related Queries"])
            
        return df_queries
    
    except (KeyError, IndexError, TypeError) as e:
        st.error(f"Could not extract related queries. Error: {e}")
        return pd.DataFrame(columns=["Related Queries"])

def convert_df_to_excel(df):
    """Convert DataFrame to Excel bytes for download"""
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')
    return output.getvalue()

def main():
    st.set_page_config(
        page_title="Perplexity JSON Analyzer",
        page_icon="🔍",
        layout="wide"
    )
    
    st.title("🔍 Perplexity Conversation Analyzer")
    st.markdown("Upload a Perplexity conversation JSON file to extract linked mentions and related queries.")
    
    # File upload
    uploaded_file = st.file_uploader(
        "Choose a JSON file", 
        type="json",
        help="Upload the JSON export from your Perplexity conversation"
    )
    
    if uploaded_file is not None:
        try:
            # Load JSON data
            json_data = json.load(uploaded_file)
            
            st.success("✅ JSON file loaded successfully!")
            
            # Show basic file info
            with st.expander("📄 File Information"):
                try:
                    conversation_title = json_data.get('entries', [{}])[0].get('title', 'Unknown')
                    st.write(f"**Conversation Title:** {conversation_title}")
                    st.write(f"**File size:** {len(str(json_data))} characters")
                except:
                    st.write("Basic file information extracted")
            
            # Create two columns for the results
            col1, col2 = st.columns(2)
            
            # Extract and display web results (linked mentions)
            with col1:
                st.subheader("🔗 Linked Mentions")
                web_df = extract_web_results(json_data)
                
                if not web_df.empty:
                    st.success(f"Found {len(web_df)} linked mentions")
                    
                    # Display the table
                    st.dataframe(web_df, use_container_width=True)
                    
                    # Download button for web results
                    excel_data = convert_df_to_excel(web_df)
                    st.download_button(
                        label="📥 Download Linked Mentions (Excel)",
                        data=excel_data,
                        file_name="linked_mentions.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )
                else:
                    st.warning("No related queries found in the uploaded file.")
                st.warning("No linked mentions found in the uploaded file.")
            
            # Extract and display related queries
            with col2:
                st.subheader("❓ Related Queries")
                queries_df = extract_related_queries(json_data)
                
                if not queries_df.empty:
                    st.success(f"Found {len(queries_df)} related queries")
                    
                    # Display the table
                    st.dataframe(queries_df, use_container_width=True)
                    
                    # Download button for related queries
                    excel_data_queries = convert_df_to_excel(queries_df)
                    st.download_button(
                        label="📥 Download Related Queries (Excel)",
                        data=excel_data_queries,
                        file_name="related_queries.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )
                else:
                
        
        except json.JSONDecodeError:
            st.error("❌ Invalid JSON file. Please upload a valid JSON file from Perplexity.")
        except Exception as e:
            st.error(f"❌ An error occurred while processing the file: {str(e)}")
            with st.expander("Debug Information"):
                st.code(traceback.format_exc())
    
    else:
        # Instructions when no file is uploaded
        st.info("👆 Please upload a Perplexity conversation JSON file to begin analysis.")
        
        with st.expander("ℹ️ How to use this app"):
            st.markdown("""
            1. **Export your conversation** from Perplexity as a JSON file
            2. **Upload the file** using the file uploader above
            3. **View the results** in two tables:
               - **Linked Mentions**: All web sources referenced in the conversation
               - **Related Queries**: Suggested follow-up questions
            4. **Download** the results as Excel files for further analysis
            
            **Expected JSON Structure:**
            The app looks for data in this structure:
            ```
            {
              "entries": [
                {
                  "title": "Conversation title",
                  "blocks": [...],
                  "related_queries": [...]
                }
              ]
            }
            ```
            """)

if __name__ == "__main__":
    main()
