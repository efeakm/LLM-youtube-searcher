import streamlit as st
from utils import get_youtube_videos_with_prompt

def main():
    # Page configuration
    st.set_page_config(
        page_title="YouTube Video Info Fetcher 🎬",
        page_icon="🎬",
        layout="centered", # Use a centered layout
        initial_sidebar_state="collapsed"
    )

    st.title('YouTube Video Info Fetcher 🎬')

    # Style the text input and button with some background color and padding
    st.markdown("""
    <style>
        .stTextInput, .stButton>button {
            background-color: #f0f0f0;
            padding: 10px;
            border-radius: 5px;
            border: 1px solid #ddd;
        }
        .stButton>button:hover {
            background-color: #ddd;
        }
    </style>
    """, unsafe_allow_html=True)

    # Input prompt
    prompt = st.text_input("Enter your prompt:")

    if st.button("Fetch YouTube Info"):
        video_infos = get_youtube_videos_with_prompt(prompt)
        
        # Add a little space after the prompt button
        for i in range(3):
            st.markdown("<br>", unsafe_allow_html=True)


        # Displaying the YouTube video details
        for video_info in video_infos:
            # Centered and bold video name
            st.markdown(f"<h3 style='text-align: center; font-weight: bold; color: #4a90e2;'>{video_info['video_name']}</h3>", unsafe_allow_html=True)
            
            # Emojis for views and likes with a bit larger font size
            st.markdown(f"👁️ <span style='font-size: 18px;'>View Count: {video_info['view_count']}</span>", unsafe_allow_html=True)
            st.markdown(f"👍 <span style='font-size: 18px;'>Like Count: {video_info['like_count']}</span>", unsafe_allow_html=True)

            # Making the thumbnail clickable, leading to the video URL
            st.markdown(f"[![Video Thumbnail]({video_info['thumbnail_url']})]({video_info['video_url']})", unsafe_allow_html=True)
            
            # Adding a separator
            st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True) # Spacer
            st.markdown("---")

if __name__ == "__main__":
    main()
