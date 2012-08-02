				</div><!-- .tab-content -->
			</div><!-- .tabbable -->
		</div><!-- .span9 -->
		<div class="span3">
				
			<div id="quick-add" class="sidebar well">
				<h3>Quick Add</h3>
				<p id="add-agent">
					<a href="#add-agent-modal" class="btn" data-toggle="modal"><i class="icon-user"></i> Add Agent</a>
					<div class="modal hide fade" id="add-agent-modal">
						<div class="modal-header">
							<button type="button" class="close" data-dismiss="modal">×</button>
							<h3>Add Agent</h3>
						</div>
						<?php include('include-form-add-agent.php'); ?>
					</div>
				</p>
				<p id="add-endorsement">
					<a href="#add-endorsement-modal" class="btn" data-toggle="modal"><i class="icon-bullhorn"></i> Add Endorsement</a>
					<div class="modal hide fade" id="add-endorsement-modal">
						<div class="modal-header">
							<button type="button" class="close" data-dismiss="modal">×</button>
							<h3>Add Endorsement</h3>
						</div>
						<?php include('include-form-add-endorsement.php'); ?>
					</div>
				</p>
				<p id="add-loanrequest">
					<a href="#add-loanrequest-modal" class="btn" data-toggle="modal"><i class="icon-briefcase"></i> Add Loan Request</a>
					<div class="modal hide fade" id="add-loanrequest-modal">
						<div class="modal-header">
							<button type="button" class="close" data-dismiss="modal">×</button>
							<h3>Add Loan Request</h3>
						</div>
						<?php include('include-form-add-loanrequest.php'); ?>
					</div>
				</p>
			</div>
			
			<div class="alert alert-info">
				<h4>Developer Note: All Forms</h4>
				<ul>
					<li>Needs form validation JS.</li>
					<li>On close, wipe data if unsubmitted</li>
					<li>All items with Typeahead JS need to connect to current Agent data set.</li>
				</ul>
			</div>
			
			<div class="sidebar">
				<h3>Recent Views</h3>
				<ul>
					<li><a href="">Latest Search</a></li>
					<li><a href="">Second Latest Search</a></li>
					<li><a href="">Viewed Agent</a></li>
				</ul>
			</div>

			<div class="alert alert-info">
				<h4>Developer Note: Recent Searches</h4>
				<ul>
					<li>Load new searches</li>
				</ul>
			</div>
			
		</div><!-- .span3 -->
	</div>
</div>

<hr>
<div class="container">
    <footer class="row">
        <div class="span6">
            <p>TrustScore Demo</p>
        </div>
        <div class="span6" style="text-align:right">
            <p>TrustScore Team 2012
            </p>
        </div>
    </footer>

</div> <!-- .container -->

</body>
</html>
