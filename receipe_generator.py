import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()

MODEL_NAME = "gemini-3.5-flash"

CUISINES = ["Any", "Indian", "Italian", "Mexican", "Chinese", "Thai",
            "Mediterranean", "American", "Japanese"]
DIETS = ["Any", "Vegan", "Vegetarian", "Jain", "Gluten-free", "Keto"]


@st.cache_resource
def get_client():
    # Reads GEMINI_API_KEY / GOOGLE_API_KEY from the environment (.env supported)
    return genai.Client()


def generate_recipe(ingredients, cuisine, diet):
    """Generate a recipe using the ingredients provided."""
    prompt = f"""
    Generate one food recipe using ingredients: {', '.join(ingredients)}
    Recipe should be more than 100 words.
    Cuisine: {cuisine}
    Diet: {diet}

    Format the answer in Markdown with:
    - A recipe title
    - Prep time, cook time and servings
    - An ingredients list with quantities
    - Numbered cooking steps
    """
    response = get_client().models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
    )
    return response.text


# ---------- UI ----------
st.set_page_config(page_title="Recipe Generator", page_icon="🍲", layout="centered")

st.title("🍲 Recipe Generator")
st.caption("Tell me what's in your kitchen and I'll suggest a recipe.")

with st.form("recipe_form"):
    ingredients_text = st.text_area(
        "Ingredients (comma separated)",
        value="tomatoes, lentil, onion, jeera, salt",
        placeholder="e.g. tomatoes, lentil, onion, jeera, salt",
    )
    col1, col2 = st.columns(2)
    cuisine = col1.selectbox("Cuisine", CUISINES, index=CUISINES.index("Indian"))
    diet = col2.selectbox("Diet", DIETS, index=DIETS.index("Vegan"))
    submitted = st.form_submit_button("Generate Recipe", use_container_width=True)

if submitted:
    ingredients = [i.strip() for i in ingredients_text.split(",") if i.strip()]

    if not ingredients:
        st.warning("Please enter at least one ingredient.")
    else:
        try:
            with st.spinner("Cooking up a recipe..."):
                recipe = generate_recipe(ingredients, cuisine, diet)
            st.session_state["recipe"] = recipe
        except Exception as e:
            st.error(f"Could not generate recipe: {e}")

if "recipe" in st.session_state:
    st.divider()
    st.markdown(st.session_state["recipe"])
    st.download_button(
        "Download recipe (.md)",
        data=st.session_state["recipe"],
        file_name="recipe.md",
        mime="text/markdown",
    )