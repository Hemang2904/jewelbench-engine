# JewelBench: Intelligent Jewelry Weight & Pricing Engine

JewelBench is an AI-powered utility designed for the modern jewelry industry. This engine automates the process of calculating precise metal weights from 3D models (STL) and provides real-time valuation based on live market prices.

## 🚀 Features

- **Automated STL Analysis**: Rapidly calculates mesh volume, surface area, and bounding box dimensions.
- **Precision Weight Estimation**: Converts volume to mass using high-accuracy density constants:
    - **Gold**: 24K (19.32 g/cm³), 22K (17.50 g/cm³), 18K (15.58 g/cm³)
    - **Silver**: 10.49 g/cm³
    - **Platinum**: 21.45 g/cm³
- **Live Market Integration**: Architecture built to consume live pricing feeds for real-time cost estimation.
- **Zero-Wait Processing**: Optimized Python-based backend using NumPy and Trimesh for high-performance mesh calculations.

## 🛠️ Tech Stack

- **Core Engine**: Python 3.9+
- **Geometry Processing**: `trimesh` (LHE mesh loading and manifold validation)
- **Mathematical Compute**: `numpy` (Vectorized geometry calculations)
- **UI Framework**: `Streamlit` (Interactive Web Portal)
- **Networking**: `requests` (API integration layer)

## 📐 Technical Implementation Detail

The engine operates on a three-stage pipeline:
1. **Mesh Validation**: Ensuring the uploaded STL is watertight (manifold) for accurate volume calculation.
2. **Volumetric Analysis**: Using the Divergence Theorem to calculate the exact volume of the complex jewelry geometry.
3. **Weight-Price Synthesis**: Applying material density constants followed by a multiplication of the `spot_price` retrieved via the pricing module.

## 📦 Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Hemang2904/jewelbench-engine.git
   cd jewelbench-engine
   ```
2. **Environment Setup**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. **Run Locally**:
   ```bash
   streamlit run app.py
   ```

## 💎 Use Cases

- **AI-Driven CAD Workflows**: Eliminate manual volume estimation in Rhino or MatrixGold.
- **Instant Quotation Systems**: Provide customers with immediate metal value estimates based on their custom designs.
- **Production Validation**: Check the weight of a design before it hits the 3D printer to manage casting costs.

---
**Lead Developer**: Hemang Shukla | **System Architect**: O.R.I.O.N. 🌌
