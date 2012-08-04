<form class="form-horizontal">
	<fieldset class="modal-body">

		<div class="alert alert-info">
			<h4>Developer Note: Endorsement Form</h4>
			<ul>
				<li>Endorsee & Endorser Name = Agent search. Uses Bootstrap Typeahead JS.</li>
				<li>Loan Types are assumed to be a limited selection with the fist option left blank.</li>
			</ul>
		</div>

		<div class="control-group">
			<label class="control-label" for="form-add-endorsement01">* Endorser</label>
			<div class="controls">
				<input type="text" class="input-xlarge" id="form-add-endorsement01" data-provide="typeahead" data-items="4" data-source="" required="required">
				<p class="help-block">An Endorser must be added as an Agent first. <a href="#add-agent-modal" data-toggle="modal" data-dismiss="modal">Add Agent</a></p>
			</div>
		</div>
		<div class="control-group">
			<label class="control-label" for="form-add-endorsement02">* Endorsee</label>
			<div class="controls">
				<input type="text" class="input-xlarge" id="form-add-endorsement02" data-provide="typeahead" data-items="4" data-source="" required="required">
				<p class="help-block">The Endorsee recieves the endorsement and must be added as an Agent first. <a href="#add-agent-modal" data-toggle="modal" data-dismiss="modal">Add Agent</a></p>
			</div>
		</div>
		<div class="control-group">
            <label class="control-label" for="form-add-endorsement03">Loan Type</label>
			<div class="controls">
				<select id="form-add-endorsement03">
					<!-- these options should be dynamic. The first option should be blank --> 
					<option></option>
					<option>Loan Type Number One</option>
					<option>Stupid Loan Type</option>
					<option>Loan Out Everything!</option>
				</select>
				<p class="help-block">Loan Type is an optional endorsement for a single action.</p>
			</div>
		</div>
		<div class="control-group">
			<label class="control-label" for="form-add-endorsement04">* Endorsement Value</label>
			<div class="controls">
				<label class="radio">
					<input type="radio" name="form-add-endorsement04" id="form-add-endorsement04a" required="required">
					<span>Positive</span>
				</label>
				<label class="radio">
					<input type="radio" name="form-add-endorsement04" id="form-add-endorsement04b" required="required">
					<span>Negative</span>
				</label>
			</div>
		</div>
	</fieldset>
	<fieldset class="modal-footer">
		<button href="#" class="btn" data-dismiss="modal">Close</button>
		<button type="submit" href="#" class="btn btn-primary">Save</button>
	</fieldset>
</form>
