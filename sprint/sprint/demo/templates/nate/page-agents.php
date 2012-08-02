<?php

$agentactions = '
<div class="btn-group">
	<button class="btn dropdown-toggle" data-toggle="dropdown"> Actions&hellip; <span class="caret"></span></button>
	<ul class="dropdown-menu">
		<li><a href="#">Add Recommendation</a></li>
		<li><a href="#">Add Loan Request</a></li>
	</ul>
</div>';

?>

<section class="tab-pane" id="tab2">
	<div class="alert alert-info">
		<h4>Developer Note:</h4>
		<ul>
			<li>open/close agent drawer. agent drawer shows current loan description (linked), and status.</li>
			<li>show agent view</li>
			<li>add agent search</li>
		</ul>
	</div>

	<header class="pane-header">
		<form class="form-search pull-right">
			<input type="text" class="search-query" placeholder="Search Agents">
		</form>
		<h2>Agents</h2>
	</header>
	<div class="pane-body">
		<table class="table table-striped">
			<thead>
				<tr>
					<th></th>
					<th>Name</th>
					<th>Trust Score</th>
					<th>Loans</th>
					<th>Actions</th>
				</tr>
			</thead>
			<tbody>
				<tr>
					<td><a href="#"><i class="icon-chevron-down"></i></a></td>
					<td><a href="#">Person's Name</a></td>
					<td>000</td>
					<td>2</td>
					<td>
						<?php echo $agentactions; ?>
					</td>
				</tr>
				<tr>
					<td colspan="6">
						<table class="table">
							<caption>Person's Name Loans</caption>
							<tbody>
								<tr>
									<td><a href="#">KV-hh9-o9</a></td>
									<td>$200</td>
									<td>This is the loan description ...</td>
									<td><span class="label label-warning">Needs Recommendation</span></td>
								</tr>
								<tr>
									<td><a href="#">KV-hh9-o9</a></td>
									<td>$200</td>
									<td>This is another loan description ...</td>
									<td><span class="label label-important">Late Payment</span></td>
								</tr>
							</tbody>
						</table>
					</td>
				</tr>
				<tr>
					<td><a href="#"><i class="icon-chevron-right"></i></a></td>
					<td><a href="#">Another Person's Name</a></td>
					<td>000</td>
					<td>20</td>
					<td>
						<?php echo $agentactions; ?>
					</td>
				</tr>
				<tr>
					<td><a href="#"><i class="icon-chevron-right"></i></a></td>
					<td><a href="#">A Third Person's Name</a></td>
					<td>000</td>
					<td>1</td>
					<td>
						<?php echo $agentactions; ?>
					</td>
				</tr>
			</tbody>
		</table>
	</div>
</section>
