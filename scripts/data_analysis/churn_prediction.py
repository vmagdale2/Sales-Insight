# Create a churn label (0 = Active, 1 = Churned)
df["churn"] = df["sales"].apply(lambda x: 1 if x == 0 else 0)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(df.drop(columns=["churn"]), df["churn"], test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)
