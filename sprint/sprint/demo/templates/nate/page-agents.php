	<section class="tab-pane" id="tab2">
		<div class="alert alert-info">
			<h4>Developer Note:</h4>
			<ul>
				<li>open/close agent drawer. agent drawer shows current loan description (linked), and status.</li>
				<li>show agent view</li>
				<li>add agent search</li>
			</ul>
		</div>

		<form class="navbar-search pull-right">
			<input type="text" class="search-query" placeholder="Search Agents">
		</form>
		<h2>Agents</h2>
		<table class="table table-striped">
			<thead>
				<tr>
					<th>Name</th>
					<th>Score</th>
					<th>Labels</th>
					<th>Actions</th>
					<th>Loans</th>
				</tr>
			</thead>
			<tbody>
				<tr>
					<td><a href="#">Person's Name</a></td>
					<td>000</td>
					<td><span class="label label-success">In Good Standing</span></td>
					<td><a href="#" class="btn btn-small"><i class="icon-bullhorn"></i> Add Endorsement</a> <a href="#" class="btn btn-small"><i class="icon-briefcase"></i> Add Loan Request</a></td>
					<td>2 <i class="icon-chevron-down"></i></td>
				</tr>
				<tr class="row-open">
					<td><a href="#">Another Person's Name</a></td>
					<td>000</td>
					<td><span class="label label-warning">Late Payment</span></td>
					<td><a href="#" class="btn btn-small"><i class="icon-bullhorn"></i> Add Endorsement</a> <a href="#" class="btn btn-small"><i class="icon-briefcase"></i> Add Loan Request</a></td>
					<td>20 <i class="icon-chevron-up"></i></td>
				</tr>
				<tr class="row-drawer">
					<td colspan="5">
						
					</td>
				</tr>
				<tr>
					<td><a href="#">A Third Person's Name</a></td>
					<td>000</td>
					<td><span class="label label-info">In Process</span></td>
					<td><a href="#" class="btn btn-small"><i class="icon-bullhorn"></i> Add Endorsement</a> <a href="#" class="btn btn-small"><i class="icon-briefcase"></i> Add Loan Request</a></td>
					<td>1 <i class="icon-chevron-down"></i></td>
				</tr>
			</tbody>
		</table>
	</section>
