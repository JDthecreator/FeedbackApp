import React from "react";
import "survey-core/defaultV2.min.css";
import { Model } from "survey-core";
import { Survey } from "survey-react-ui";

const surveyJson = {
  elements: [
    {
      name: "FirstName",
      title: "Enter your first name:",
      type: "text",
      isRequired: true,
    },
    {
      name: "LastName",
      title: "Enter your last name:",
      type: "text",
      isRequired: true,
    },
    {
        name: "feeback",
        title: "Please provide your feedback:",
        type: "text",
        isRequired: true,
    },
    {
        name: "rating",
        title: "Rating",
        type: "rating",
        isRequired: true,
        scaleColorMode: "colored",
        rateCount: 10,
        rateMax: 10,
        displayMode:"buttons"
      },
  ],
};

const FeedbackForm = () => {
  const survey = new Model(surveyJson);

  // Handle form submission
  survey.onComplete.add((sender) => {
    const data = sender.data; // Retrieve form data
    console.log("Form data submitted:", data);

    // Send the data to the FastAPI backend
    fetch("http://localhost:8000/submit-feedback/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        feedback: "Great app!",
        rating: 5,
      }),
    })
      .then((response) => response.json())
      .then((result) => {
        console.log("Server response:", result);
        alert(result.message); // Display success message
      })
      .catch((error) => {
        console.error("Error submitting feedback:", error);
        alert("There was an error submitting the feedback.");
      });
  });

  return <Survey model={survey} />;
};

const MainPage = () => {
  return (
    <div>
      <h1>Welcome to my Feedback App</h1>
      <p>Submit your feedback and view others' feedback!</p>
      <FeedbackForm />
    </div>
  );
};

export default MainPage;
