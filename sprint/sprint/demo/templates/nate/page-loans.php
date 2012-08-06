<?php

$loanactions = '
<div class="btn-group">
	<button class="btn dropdown-toggle" data-toggle="dropdown"> Actions&hellip; <span class="caret"></span></button>
	<ul class="dropdown-menu">
		<li><a href="#">Add Payment</a></li>
		<li><a href="#">Add Notification</a></li>
		<li><a href="#">Clone Loan</a></li>
	</ul>
</div>';

$loanstatusoptions = '
<ul class="dropdown-menu">
	<li><a href="#">Awaiting Action</a></li>
	<li><a href="#">In Process</a></li>
	<li><a href="#">Needs Recommendation</a></li>
	<li><a href="#">Approved</a></li>
	<li><a href="#">Defaulted</a></li>
	<li><a href="#">Closed</a></li>
</ul>'
;

?>

<section class="tab-pane" id="tab3">

	<div class="alert alert-info">
		<h4>Developer Note: Loans</h4>
		<ul>
			<li>add ordering</li>
			<li>connect Agent Names to Agent tab</li>
		</ul>
	</div>

	<header class="pane-header">
		<form class="form-search pull-right">
			<input type="text" class="search-query" placeholder="Search Loans">
		</form>
		<h2>Loans</h2>
	</header>
	<div class="pane-body">
		<table class="table table-striped">
			<thead>
				<tr>
					<th></th>
					<th>Loan ID</th>
					<th>Amount</th>
					<th>Agent Name</th>
					<th>Status</th>
					<th>Actions</th>
				</tr>
			</thead>
			<tbody>
				<tr>
					<td><a href="#"><i class="icon-chevron-down"></i></a></td>
					<td><a href="">XR-889-08</a></td>
					<td>$560</td>
					<td><a href="#">Person's Name</a></td>
					<td>
						<div class="btn-group">
							<button class="btn btn-success" href="#">Approved</button>
							<button class="btn btn-success dropdown-toggle" data-toggle="dropdown"><span class="caret"></span></button>
							<?php echo $loanstatusoptions; ?>
						</div>
					</td>
					<td>
						<?php echo $loanactions; ?>
					</td>
				</tr>
				<tr>
					<td colspan="6">
						<p><strong>Description:</strong> This is the description for the loan.</p>
					</td>
				</tr>
				<tr>
					<td><a href="#"><i class="icon-chevron-right"></i></a></td>
					<td><a href="#">KV-hh9-o9</a></td>
					<td>$200</td>
					<td><a href="#">Another Person's Name</a></td>
					<td>
						<div class="btn-group">
							<button class="btn btn-warning" href="#">Needs Recommendation</button>
							<button class="btn btn-warning dropdown-toggle" data-toggle="dropdown"><span class="caret"></span></button>
							<?php echo $loanstatusoptions; ?>
						</div>
					</td>
					<td>
						<?php echo $loanactions; ?>
					</td>
				</tr>
				<tr>
					<td><a href="#"><i class="icon-chevron-right"></i></a></td>
					<td><a href="#">KV-hh9-o9</a></td>
					<td>$200</td>
					<td><a href="#">Another Person's Name</a></td>
					<td>
						<div class="btn-group">
							<button class="btn btn-info" href="#">Awaiting Action</button>
							<button class="btn btn-info dropdown-toggle" data-toggle="dropdown"><span class="caret"></span></button>
							<?php echo $loanstatusoptions; ?>
						</div>
					</td>
					<td>
						<?php echo $loanactions; ?>
					</td>
				</tr>
				<tr>
					<td><a href="#"><i class="icon-chevron-right"></i></a></td>
					<td><a href="#">KV-hh9-o9</a></td>
					<td>$200</td>
					<td><a href="#">Another Person's Name</a></td>
					<td>
						<div class="btn-group">
							<button class="btn btn-primary" href="#">In Process</button>
							<button class="btn btn-primary dropdown-toggle" data-toggle="dropdown"><span class="caret"></span></button>
							<?php echo $loanstatusoptions; ?>
						</div>
					</td>
					<td>
						<?php echo $loanactions; ?>
					</td>
				</tr>
				<tr>
					<td><a href="#"><i class="icon-chevron-right"></i></a></td>
					<td><a href="#">KV-hh9-o9</a></td>
					<td>$200</td>
					<td><a href="#">Another Person's Name</a></td>
					<td>
						<div class="btn-group">
							<button class="btn btn-danger" href="#">Defaulted</button>
							<button class="btn btn-danger dropdown-toggle" data-toggle="dropdown"><span class="caret"></span></button>
							<?php echo $loanstatusoptions; ?>
						</div>
					</td>
					<td>
						<?php echo $loanactions; ?>
					</td>
				</tr>
				<tr>
					<td><a href="#"><i class="icon-chevron-right"></i></a></td>
					<td><a href="#">KV-hh9-o9</a></td>
					<td>$200</td>
					<td><a href="#">Another Person's Name</a></td>
					<td>
						<div class="btn-group">
							<button class="btn btn-inverse" href="#">Closed</button>
							<button class="btn btn-inverse dropdown-toggle" data-toggle="dropdown"><span class="caret"></span></button>
							<?php echo $loanstatusoptions; ?>
						</div>
					</td>
					<td>
						<?php echo $loanactions; ?>
					</td>
				</tr>
			</tbody>
		</table>
	</div>
</section>