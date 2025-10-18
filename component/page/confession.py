import streamlit as st
import component.function.dialogs as dialogs
from component.function import images, audio
import logging
import streamlit_antd_components as sac

st.set_page_config(page_title="Confession", page_icon="❤️", layout="centered")

@st.fragment()
def fragment():
    
    if 'story_key' not in st.session_state:
        st.session_state.story_key = 1

    if 'dialog_key' not in st.session_state:
        st.session_state.dialog_key = 0

    if 'answer_quesion' not in st.session_state:
        st.session_state.answer_quesion = False

    if 'end' not in st.session_state:
        st.session_state.end = False

    if 'accept' not in st.session_state:
        st.session_state.accept = False
    
    try:
        story = st.secrets["story"][str(st.session_state.story_key)]
    except KeyError:
        st.session_state.story_key = st.session_state.story_key - 1
        st.session_state.end = True
        st.rerun(scope="fragment")


    if st.session_state.end is False:
        
        st.session_state.default_dialog = story["dialogs"][st.session_state.dialog_key]

        with st.container():
            
            left,right = st.columns([4,6])
            
            with left.container(height="stretch",border=False,vertical_alignment="center",horizontal_alignment="center"):
                logging.info(f"story-{st.session_state.story_key}_dialog-{st.session_state.dialog_key}")
                st.markdown(images.load_img_html(f"static/{st.session_state.story_key}/{st.session_state.dialog_key}.png"),unsafe_allow_html=True)
                st.write("\n")
                st.audio("static/bgm.mp3", loop=True, autoplay=True)
                
            with right.container(border=True,height="stretch",vertical_alignment="top",horizontal_alignment="center"):
                place_holder = st.empty()
                
            sac.divider(label='ラン', icon='heart', align='center', color='gray')

            with st.container(border=False,vertical_alignment="center",horizontal_alignment="center"):
                
                inner_left, inner_right = st.columns(2, vertical_alignment= "center")

                if story.question is False:
                    if inner_left.button("Next", icon=":material/fast_forward:" , type="primary", disabled=st.session_state.end, use_container_width=True, width="stretch"):
                        if st.session_state.dialog_key < story.count-1:
                            st.session_state.dialog_key += 1
                            st.session_state.default_dialog = story["dialogs"][st.session_state.dialog_key]
                            st.rerun(scope="fragment")
                                                
                        else: 
                            st.session_state.story_key += 1
                            st.session_state.dialog_key = 0
                            st.session_state.default_dialog = story["dialogs"][st.session_state.dialog_key]
                            st.rerun(scope="fragment")
                            
                else:
                    if st.session_state.answer_quesion is False:
                        with inner_left.popover("Options",disabled=st.session_state.end, use_container_width=True, width="stretch"):
                            if st.button(key="Yes", label=story["dialogs"][1], icon=":material/check:" , type="tertiary", use_container_width=True):
                                st.session_state.answer_quesion = True
                                st.session_state.dialog_key = 2
                                
                                if st.session_state.story_key == 7:
                                    st.session_state.accept = True                            
                                st.rerun(scope="fragment")
                                
                            if st.button(key="No", label=story["dialogs"][3], icon=":material/close:" , type="tertiary", use_container_width=True):
                                st.session_state.answer_quesion = True
                                st.session_state.dialog_key = 4
                                st.rerun(scope="fragment")
                                
                    else:
                        if inner_left.button("Next", icon=":material/fast_forward:" , type="primary", disabled=st.session_state.end, use_container_width=True, width="stretch"):
                            if st.session_state.dialog_key in [2,4]:
                                st.session_state.dialog_key = 5
                                st.rerun(scope="fragment")
                                
                            elif st.session_state.dialog_key == 5: 
                                st.session_state.story_key += 1
                                st.session_state.dialog_key = 0
                                st.session_state.answer_quesion = False
                                st.rerun(scope="fragment")
                
            
                if inner_right.button("Reset", icon=":material/restart_alt:", type="secondary", use_container_width=True, width="stretch"):
                    st.session_state.clear()
                    st.rerun(scope="fragment")


            with place_holder:
                if story.question is False:
                    st.write_stream(dialogs.stream_data(story["dialogs"][st.session_state.dialog_key]))
                else:
                    st.write_stream(dialogs.stream_data(st.session_state.default_dialog))

    else:
        if st.session_state.accept:
            st.balloons()
            sac.result(label='200 SUCCESS', description=st.secrets["result"]["accept"], status='success')
        else:
            sac.result(label="418 I'M A TEAPOT", description=st.secrets["result"]["deny"], status='warning')

st.html("component/style/image.html")

fragment()