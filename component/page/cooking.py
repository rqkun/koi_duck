import streamlit as st
import component.function.email as email
import component.constants as constants

st.set_page_config(page_title="Racoon Chef", page_icon="🍳", layout="centered")

st.markdown("""
<style>
    .footer {
        margin-top: 3rem;
        text-align: center;
        color: #888;
        font-size: 0.9em;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>🍽️ Racoon Chef</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#555;'>Select ingredients, discover recipes, and send your plan to the racoon!</p>", unsafe_allow_html=True)

ingredients = constants.INGREDIENTS
recipe_db = constants.RECIPES

with st.container(border=True):
    st.markdown("### 🥘 Ingredient Selection")
    selections = {}
    recipe_l, recipe_r = st.columns(2, gap="medium")

    selections["Main"] = [recipe_l.radio("Main",key="Main", horizontal=True, options=ingredients["Main"]["options"], width="stretch")]
    selections["Sides"] = recipe_r.multiselect("Sides", ingredients["Sides"]["options"], max_selections=ingredients["Sides"]["max_choice"], key="Sides")
    selections["Veggies"] = st.multiselect("Veggies", ingredients["Veggies"]["options"], max_selections=ingredients["Veggies"]["max_choice"], key="Veggies")

    def find_matching_recipes(selections):
        chosen = []
        for v in selections.values():
            if isinstance(v, list):
                chosen.extend(v)
            elif v != "-- Choose one --":
                chosen.append(v)
        chosen = set(chosen)

        if not chosen:
            return []

        scored = []
        for recipe in recipe_db:
            overlap = len(chosen.intersection(recipe["ingredients"]))
            if overlap > 0:
                match_percent = round((overlap / len(recipe["ingredients"])) * 100)
                scored.append({"name": recipe["name"], "ingredients": recipe["ingredients"], "match_percent": match_percent})

        scored.sort(key=lambda r: r["match_percent"], reverse=True)
        return scored

    matching_recipes = find_matching_recipes(selections)

    st.markdown("### 🍳 Suggested Recipes")
    selected_recipes = []
    if not matching_recipes:
        st.info("Select at least one ingredient to see recipe suggestions.")
    else:
        with st.container(horizontal=True, vertical_alignment="center", horizontal_alignment="center"):
            for recipe in matching_recipes:
                if st.checkbox(f"*{recipe['name']}*", key=f"recipe_{recipe['name']}"):
                        selected_recipes.append(recipe)

    noti_l, noti_r = st.columns([2,1], gap="medium", vertical_alignment="center")
    
    noti = noti_l.container()

noti = st.container()

with noti_r.container(width="stretch", vertical_alignment="center", horizontal=True, horizontal_alignment="center"):
    if st.button("Submit Ingredients 🍲", type="primary", use_container_width=True):
        if "-- Choose one --" in selections.values():
            noti.warning("Please choose one ingredient for each category before submitting.")
        else:
            with noti_l, st.spinner(show_time=True, text="Sending..."):
                email.send(selections, selected_recipes)
                noti.success(f"✅ Send successfully!")

st.markdown("<div class='footer'>🍀 Made with love.</div>", unsafe_allow_html=True)