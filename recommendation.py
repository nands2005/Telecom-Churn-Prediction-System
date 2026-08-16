def generate_recommendation(prediction, probability, sentiment):

    recommendations = []

    # High Risk Customers (80%+)
    if probability >= 80:
        recommendations = [
            "🚨 High churn risk detected.",
            "Offer an exclusive discount or retention package.",
            "Assign a dedicated customer support executive.",
            "Resolve all reported complaints immediately.",
            "Schedule a follow-up call within 24-48 hours."
        ]

    # Medium Risk Customers (50-79%)
    elif probability >= 50:
        recommendations = [
            "⚠️ Moderate churn risk.",
            "Provide personalized offers or service upgrades.",
            "Contact the customer to understand their concerns.",
            "Monitor customer activity over the next few weeks."
        ]

    # Low Risk + Negative Sentiment
    elif sentiment == "Negative":
        recommendations = [
            "Customer is unlikely to churn but has expressed dissatisfaction.",
            "Resolve the reported issue promptly.",
            "Follow up after resolving the complaint.",
            "Monitor customer satisfaction."
        ]

    # Low Risk + Positive Sentiment
    else:
        recommendations = [
            "Customer is satisfied and has a low churn risk.",
            "Send a thank-you message.",
            "Offer loyalty rewards or promotional benefits.",
            "Recommend suitable premium plans."
        ]

    return recommendations