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
import React from "react";
import axios from "axios";

// Authentication layout components
import BasicLayout from "layouts/authentication/components/BasicLayout";

// Images
import bgImage from "assets/images/bg-sign-in-basic.jpeg";
const baseURL = "http://127.0.0.1:8000/api/adminusers/";
const FORM_ENDPOINT = "http://127.0.0.1:8000/api/adminusers/";

function Basic() {
  const [rememberMe, setRememberMe] = useState(false);
  const [result, setResult] = useState();
  const handleSetRememberMe = () => setRememberMe(!rememberMe);
  const urlSearchString = window.location.search;
  const params = new URLSearchParams(urlSearchString);
  const subdivision_name = params.get("subdivision_name");

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
    console.log(event.target[0].value);
    console.log(event.target.elements.email.value);
    console.log(event.target.email.value);
    // axios
    //   .get(
    //     `http://127.0.0.1:8000/api/adminusers/?email=${event.target.email.value}&password=${event.target.password.value}`
    //   )
    axios
      .get(
        `http://${process.env.REACT_APP_IP_SERVER_BACKEND}:${process.env.REACT_APP_PORT_BACK_END}/api/getuser/?email=${event.target.email.value}&password=${event.target.password.value}`
      )
      .then((res) => {
        console.log(res);
        console.log("data aqui");
        if (res.data == "") {
          // console.log("USER NOT FOUND");
          color = "error";
          hidden = true;
          message = "USUARIO NO EXISTE - VERIFICAR USARIO Y CONTRASENA";
          mydiv = (
            <div>
              <MDAlert color="error" dismissible>
                {message}
              </MDAlert>
            </div>
          );
          setResult(mydiv);
        } else {
          color = "success";
          hidden = true;
          message = "USER FOUND";
          mydiv = (
            <div>
              <MDAlert color="success" dismissible>
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
            Bienvenid@
          </MDTypography>
          <MDTypography variant="h4" fontWeight="medium" color="white" mt={1}>
            {subdivision_name}
          </MDTypography>
          <Grid container spacing={3} justifyContent="center" sx={{ mt: 1, mb: 2 }}>
            <Grid item xs={2}>
              <MDTypography component={MuiLink} href="#" variant="body1" color="white">
                <FacebookIcon color="inherit" />
              </MDTypography>
            </Grid>
            <Grid item xs={2}>
              <MDTypography component={MuiLink} href="#" variant="body1" color="white">
                <GitHubIcon color="inherit" />
              </MDTypography>
            </Grid>
            <Grid item xs={2}>
              <MDTypography component={MuiLink} href="#" variant="body1" color="white">
                <GoogleIcon color="inherit" />
              </MDTypography>
            </Grid>
          </Grid>
        </MDBox>
        <MDBox pt={4} pb={3} px={3}>
          <MDBox component="form" role="form" onSubmit={handleSubmit}>
            <MDBox mb={2}>
              <MDInput type="email" name="email" label="Email" fullWidth />
            </MDBox>
            <MDBox mb={2}>
              <MDInput type="password" name="password" label="Password" fullWidth />
            </MDBox>
            <MDBox display="flex" alignItems="center" ml={-1}>
              <Switch checked={rememberMe} onChange={handleSetRememberMe} />
              <MDTypography
                variant="button"
                fontWeight="regular"
                color="text"
                onClick={handleSetRememberMe}
                sx={{ cursor: "pointer", userSelect: "none", ml: -1 }}
              >
                &nbsp;&nbsp;Remember me
              </MDTypography>
            </MDBox>
            <MDBox mt={4} mb={1}>
              <MDButton variant="gradient" color="info" type="submit" fullWidth>
                sign in
              </MDButton>
            </MDBox>
            <MDBox mt={3} mb={1} textAlign="center">
              <MDTypography variant="button" color="text">
                Don&apos;t have an account?{" "}
                <MDTypography
                  component={Link}
                  to="/authentication/sign-up"
                  variant="button"
                  color="info"
                  fontWeight="medium"
                  textGradient
                >
                  Sign up
                </MDTypography>
              </MDTypography>
            </MDBox>
          </MDBox>
        </MDBox>
        {result}
      </Card>
    </BasicLayout>
  );
}

export default Basic;
