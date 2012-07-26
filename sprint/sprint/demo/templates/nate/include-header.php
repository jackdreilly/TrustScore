<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>TrustScore Dashboard</title>
	<link rel="stylesheet" href="bootstrap/css/bootstrap.css">
	<link rel="stylesheet" href="bootstrap/css/bootstrap-responsive.css">
	<link rel="stylesheet" href="css/style.css">
    <!--[if lt IE 9]>
    <script src="//html5shim.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->
    <script type="text/javascript" src="js/jquery-1.7.2.min.js"></script>
	<script type="text/javascript" src="bootstrap/js/bootstrap.js"></script>
</head>

<body>

<div class="navbar navbar-fixed-top">
    <div class="navbar-inner">
        <div class="container">
			<img class="brand" src="img/logo.png" alt="TrustScore" />
			<h1 class="brand">Dashboard</h1>
			<div class="nav-collapse">
				<form class="navbar-search pull-right">
				  <input type="text" class="search-query" placeholder="Search Everything">
				</form>
			</div>
        </div>
    </div>
</div>

<div class="container">
	<div class="row">
		<div class="span9">

			<div class="tabbable">
				<ul class="nav nav-tabs">
					<li class="active"><a href="#tab1" data-toggle="tab">Action Items</a></li>
					<li><a href="#tab2" data-toggle="tab">Agents</a></li>
					<li><a href="#tab3" data-toggle="tab">Loans</a></li>
					<li><a href="#tab4" data-toggle="tab">Search Results (temp tab)</a></li>
				</ul>
				<div class="tab-content">
