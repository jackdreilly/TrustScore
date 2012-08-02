<form class="form-horizontal">
	<fieldset class="modal-body">

		<div class="alert alert-info">
			<h4>Developer Note: Loan Request Form</h4>
			<ul>
				<li>Endorsee Name = Agent search. Uses Bootstrap Typeahead JS.</li>
				<li>What are the Loan Properties?</li>
			</ul>
		</div>

		<div class="control-group">
			<label class="control-label" for="form-add-loanrequest01">* Endorsee Name</label>
			<div class="controls">
				<input type="text" class="input-xlarge" id="form-add-endorsement01" data-provide="typeahead" data-items="4" data-source="" required="required">
				<p class="help-block">An Endorsee must be added as an Agent first. <a href="#add-agent-modal" data-toggle="modal" data-dismiss="modal">Add Agent</a></p>
			</div>
		</div>
		<div class="control-group">
			<label class="control-label" for="form-add-loanrequst02">* Amount Requested</label>
			<div class="controls">
				<div class="input-prepend">
					<span class="add-on">$</span><input type="text" class="input-large" id="form-add-loanrequst02" required="required"/>
				</div>
			</div>
		</div>
		<div class="control-group">
			<label class="control-label" for="form-add-loanrequest03">Loan Properties ???</label>
			<div class="controls">
				<select id="form-add-loanrequest03">
					<!-- these options should be dynamic. The first option should be blank --> 
					<option></option>
					<option>Loan Type Number One</option>
					<option>Stupid Loan Type</option>
					<option>Loan Out Everything!</option>
				</select>
			</div>
		</div>
	</fieldset>
	<fieldset class="modal-footer">
		<button href="#" class="btn" data-dismiss="modal">Close</button>
		<button type="submit" href="#" class="btn btn-primary">Save</button>
	</fieldset>
</form>
