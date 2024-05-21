import { func } from "prop-types";
import useForm from "./useForm";
import MDAlert from "components/MDAlert";
import axios from "axios";
import { useState } from "react";

const FORM_ENDPOINT = "http://127.0.0.1:8000/api/subdivision/"; // TODO - update to the correct endpoint

const Form = () => {
  const additionalData = {
    sent: new Date().toISOString(),
  };

  const { handleSubmit, status, message } = useForm({
    additionalData,
  });
  console.log(status);
  if (status === "success") {
    return (
      <>
        <div>
          <MDAlert color="success" dismissible>
            Thank You. {message}
          </MDAlert>
        </div>
      </>
    );
  }

  if (status === "error") {
    return (
      <>
        <div>
          <MDAlert color="error" dismissible>
            {message}
          </MDAlert>
        </div>
      </>
    );
  }

  return (
    <>
      <form action={FORM_ENDPOINT} onSubmit={handleSubmit} method="POST">
        <div>
          <input type="text" placeholder="Type Division" name="typedivision" required />
        </div>
        <div>
          <input type="text" placeholder="Division Name" name="subdivision_name" required />
        </div>
        <div>
          <input type="text" placeholder="Address" name="address" required />
        </div>
        <div>
          <input type="text" placeholder="Postal Code" name="cp" required />
        </div>
        {/* <div>
      <input type="email" placeholder="Division Name" name="subdivision_name" required />
    </div> */}
        <div>
          <textarea placeholder="Add representatives" name="representatives" required />
        </div>
        <button type="submit">Send data</button>
      </form>
      <br></br>
    </>
  );
};

export default Form;
