"""
app.py — Interactive Crop Recommendation CLI
Run: python app.py
"""

import os
import sys

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
from model import generate_dataset, train_model, save_model, load_model, recommend_crop

MODEL_PATH = "model.pkl"

CROP_INFO = {
    "rice":        {"emoji": "🌾", "season": "Kharif",  "tip": "Needs flooded fields and high humidity."},
    "wheat":       {"emoji": "🌿", "season": "Rabi",    "tip": "Thrives in cool, dry climates."},
    "maize":       {"emoji": "🌽", "season": "Kharif",  "tip": "Needs moderate rainfall and good drainage."},
    "chickpea":    {"emoji": "🫘", "season": "Rabi",    "tip": "Drought-tolerant; avoid waterlogging."},
    "kidneybeans": {"emoji": "🫘", "season": "Kharif",  "tip": "Needs well-drained loamy soil."},
    "pigeonpeas":  {"emoji": "🌱", "season": "Kharif",  "tip": "Excellent for dry, semi-arid regions."},
    "mothbeans":   {"emoji": "🌱", "season": "Kharif",  "tip": "Very drought-resistant crop."},
    "mungbean":    {"emoji": "🫘", "season": "Zaid",    "tip": "Short-duration; good for crop rotation."},
    "blackgram":   {"emoji": "🫘", "season": "Kharif",  "tip": "Grows well in black cotton soil."},
    "lentil":      {"emoji": "🌿", "season": "Rabi",    "tip": "Nitrogen-fixing; improves soil health."},
    "cotton":      {"emoji": "🌸", "season": "Kharif",  "tip": "Needs deep, well-drained black soil."},
}


def banner():
    print("\n" + "=" * 50)
    print("   🌾  CROP RECOMMENDATION SYSTEM  🌾")
    print("   Powered by Machine Learning (Random Forest)")
    print("=" * 50)


def get_float(prompt, lo, hi):
    while True:
        try:
            val = float(input(f"  {prompt} [{lo}–{hi}]: "))
            if lo <= val <= hi:
                return val
            print(f"  ⚠️  Please enter a value between {lo} and {hi}.")
        except ValueError:
            print("  ⚠️  Please enter a valid number.")


def get_inputs():
    print("\n📋 Enter your soil & weather details:\n")
    N           = get_float("Nitrogen (N) content in soil (kg/ha)", 0, 200)
    P           = get_float("Phosphorus (P) content in soil (kg/ha)", 0, 200)
    K           = get_float("Potassium (K) content in soil (kg/ha)", 0, 200)
    temperature = get_float("Temperature (°C)", 0, 50)
    humidity    = get_float("Humidity (%)", 0, 100)
    ph          = get_float("Soil pH", 0, 14)
    rainfall    = get_float("Rainfall (mm)", 0, 400)
    return N, P, K, temperature, humidity, ph, rainfall


def show_results(results):
    print("\n" + "-" * 50)
    print("🏆  TOP CROP RECOMMENDATIONS FOR YOUR LAND")
    print("-" * 50)
    medals = ["🥇", "🥈", "🥉"]
    for i, r in enumerate(results):
        crop = r["crop"]
        info = CROP_INFO.get(crop, {"emoji": "🌱", "season": "—", "tip": ""})
        print(f"\n  {medals[i]} {info['emoji']}  {crop.upper()}  ({r['confidence']}% match)")
        print(f"       Season : {info['season']}")
        print(f"       Tip    : {info['tip']}")
    print("\n" + "-" * 50)


def ensure_model():
    if not os.path.exists(MODEL_PATH):
        print("\n⚙️  No trained model found. Training now (one-time setup)...")
        os.makedirs("data", exist_ok=True)
        df = generate_dataset()
        df.to_csv("data/crop_data.csv", index=False)
        model, le, _ = train_model(df)
        save_model(model, le, MODEL_PATH)
    return load_model(MODEL_PATH)


def main():
    banner()
    model, le = ensure_model()

    while True:
        inputs = get_inputs()
        results = recommend_crop(model, le, *inputs)
        show_results(results)

        print("\n  Would you like to try another prediction?")
        again = input("  Enter 'y' to continue or any other key to exit: ").strip().lower()
        if again != "y":
            print("\n  🌱 Thank you for using the Crop Recommendation System!")
            print("  Happy farming! 👨‍🌾\n")
            break


if __name__ == "__main__":
    main()
