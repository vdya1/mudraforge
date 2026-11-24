# MudraForge

MudraForge is an accessible vision-based interaction system that translates physical hand gestures captured by a standard webcam into desktop control inputs. By combining landmark tracking with lightweight machine learning classification and prediction temporal smoothing, the platform provides a responsive, user-trainable interface for hands-free computer control without requiring specialized hardware or proprietary cloud APIs.

**Pipeline:**
Webcam -> MediaPipe Hands (21 landmarks) -> Normalized 63-feature vector -> Scikit-Learn Classifier -> Prediction Smoother -> Action Controller

**Status: initial skeleton**

## Repository Structure

```text
mudraforge/
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── app.py
├── dashboard.py
├── config/
│   └── mapping.json
├── data/
│   └── .gitkeep
├── docs/
│   └── .gitkeep
├── models/
│   └── .gitkeep
├── results/
│   └── .gitkeep
├── scripts/
│   └── check_env.py
├── src/
│   ├── __init__.py
│   ├── actions.py
│   ├── features.py
│   ├── hand_tracker.py
│   ├── recognizer.py
│   ├── recorder.py
│   └── trainer.py
└── tests/
    └── test_smoke.py
```

## Installation

### Windows
```cmd
python -m venv venv
venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

### macOS / Linux
```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## How to run

- **Run Desktop Application:**
  ```bash
  python app.py
  ```

- **Run Streamlit Dashboard:**
  ```bash
  streamlit run dashboard.py
  ```

- **Run Test Suite:**
  ```bash
  pytest
  ```

## Results

## Related Work

## Future Scope
