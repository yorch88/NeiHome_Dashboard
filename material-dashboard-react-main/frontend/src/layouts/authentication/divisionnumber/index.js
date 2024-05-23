/**
=========================================================
* Material Dashboard 2 React - v2.2.0
=========================================================

* Product Page: https://www.creative-tim.com/product/material-dashboard-react
* Copyright 2023 Creative Tim (https://www.creative-tim.com)

Coded by www.creative-tim.com

 =========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
*/

import { useState } from "react";

// react-router-dom components
import { Link } from "react-router-dom";

// @mui material components
import Card from "@mui/material/Card";
import Switch from "@mui/material/Switch";
import Grid from "@mui/material/Grid";
import MuiLink from "@mui/material/Link";
import MDAlert from "components/MDAlert";
// @mui icons
import FacebookIcon from "@mui/icons-material/Facebook";
import GitHubIcon from "@mui/icons-material/GitHub";
import GoogleIcon from "@mui/icons-material/Google";

// Material Dashboard 2 React components
import MDBox from "components/MDBox";
import MDTypography from "components/MDTypography";
import MDInput from "components/MDInput";
import MDButton from "components/MDButton";
import { useNavigate } from "react-router-dom";
import React from "react";
import axios from "axios";
axios.defaults.withCredentials = true;
// Authentication layout components
import BasicLayout from "layouts/authentication/components/BasicLayout";

// Images
import bgImage from "assets/images/bg-sign-in-basic.jpeg";
const baseURL = "http://127.0.0.1:8000/api/adminusers/";
const FORM_ENDPOINT = "http://127.0.0.1:8000/api/adminusers/";

function Divisionnumber() {
  const [toDashboard, setToDashboard] = React.useState(false);
  const [rememberMe, setRememberMe] = useState(false);
  const [result, setResult] = useState();
  const handleSetRememberMe = () => setRememberMe(!rememberMe);
  const navigate = useNavigate();
  const [post, setPost] = React.useState(null);
  const state = {
    email: "",
    password: "",
  };
  let message = "";
  let color = "";
  let hidden = false;
  let mydiv = <div>Please fill</div>;
  const handleSubmit = (event) => {
    event.preventDefault();
    // console.log(event.target[0].value);
    // console.log(event.target.elements.email.value);
    // console.log(event.target.email.value);
    axios
      .get(
        `http://${process.env.REACT_APP_IP_SERVER_BACKEND}:${process.env.REACT_APP_PORT_BACK_END}/api/getdbnumber/?db_number=${event.target.db_number.value}`,
        {
          headers: {
            "Content-Type": "application/json",
          },
        }
      )
      .then((res) => {
        if (res.data !== "") {
          // setResult(res.data[0]);
          console.log(res.data[0]);
          // navigate(`"/`);
          window.location.href = `./sign-in?subdivision_name=${res.data[0].subdivision_name}`;
          // return <Navigate to="./sign-in" />;
        } else {
          color = "error";
          hidden = true;
          message = "No se encontro usuario.";
          mydiv = (
            <div>
              <MDAlert color="error" dismissible>
                {message}
              </MDAlert>
            </div>
          );
          setResult(mydiv);
        }
        console.log(color, hidden, message);
        console.log(res.data);
      });
  };
  return (
    <BasicLayout image={bgImage}>
      <Card>
        <MDBox
          variant="gradient"
          bgColor="info"
          borderRadius="lg"
          coloredShadow="info"
          mx={2}
          mt={-3}
          p={2}
          mb={1}
          textAlign="center"
        >
          <MDTypography variant="h4" fontWeight="medium" color="white" mt={1}>
            Bienvenido a NeiHome
          </MDTypography>
        </MDBox>
        <MDBox pt={4} pb={3} px={3}>
          <MDBox
            component="form"
            role="form"
            onSubmit={handleSubmit}
            // afterSubmit={() => toDashboard(true)}
          >
            <MDBox mb={2}>
              <MDInput type="text" name="db_number" label="No. de usuario" fullWidth />
            </MDBox>
            <MDBox mt={4} mb={1}>
              <MDButton variant="gradient" color="info" type="submit" fullWidth>
                Entrar
              </MDButton>
            </MDBox>
          </MDBox>
        </MDBox>
        {result}
      </Card>
    </BasicLayout>
  );
}

export default Divisionnumber;
