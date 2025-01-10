```markdown
# New York Housing Market Price Analysis

This project analyzes the real estate market in New York City by examining the price per square foot (Price per Sqft) for different properties and localities. The analysis is performed using a dataset containing housing prices, property square footage, and locality information.

## Features

- **Price per Sqft Calculation**: Calculates the price per square foot for each property in the dataset.
- **Locality-wise Average Price per Sqft**: Computes the average price per square foot for each locality in New York City.
- **Data Overview**: Displays a data table summarizing key information, including price, square footage, and price per square foot.
- **Price per Sqft Distribution**: Visualizes the overall distribution of price per square foot for the entire dataset.
- **Average Price per Sqft by Locality**: Displays a bar chart comparing the average price per square foot for different localities in New York.
- **Interactive Locality Analysis**: Allows users to select a specific locality to view detailed data and price distribution within that area.

## Technologies Used

- **Pandas**: Data manipulation and analysis.
- **Streamlit**: Web application for interactive data exploration.
- **Matplotlib**: Data visualization.
- **Seaborn**: Statistical data visualization.

## Installation

1. Clone this repository.
   ```bash
   git clone https://github.com/yourusername/new-york-housing-market-price-analysis.git
   ```

2. Install the required libraries.
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app.
   ```bash
   streamlit run app.py
   ```

## Dataset

The dataset used in this analysis contains housing data from New York City, including property prices, square footage, and locality. Ensure the dataset is placed in the correct directory (`data/newyork-housing-market.csv`) for the app to work correctly.

## Usage

- Upon running the app, you will see an overview of the dataset and can interactively explore the data by selecting different localities.
- Visualizations will update based on the selected locality, providing insights into price per square foot distribution.

## License

This project is licensed under the MIT License - see the License file for details.

## Acknowledgments

- Dataset Source: [New York Housing Market](https://www.kaggle.com/datasets/nelgiriyewithana/new-york-housing-market) (Note: Replace with the actual source if applicable).
```