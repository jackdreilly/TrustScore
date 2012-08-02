<form class="form-horizontal">
	<fieldset class="modal-body">

		<div class="alert alert-info">
			<h4>Developer Note: Add Agent Form</h4>
			<ul>
				<li>Should we add any any other profile info?</li>
			</ul>
		</div>

		<div class="control-group">
			<label class="control-label" for="form-add-agent02">* First Name</label>
			<div class="controls">
				<input type="text" class="input-xlarge" id="form-add-agent02" required="required"/>
			</div>
		</div>
		<div class="control-group">
			<label class="control-label" for="form-add-agent01">* Last Name</label>
			<div class="controls">
				<input type="text" class="input-xlarge" id="form-add-agent01" required="required"/>
			</div>
		</div>
		<div class="control-group">
			<label class="control-label" for="form-add-agent03">Credit Score</label>
			<div class="controls">
				<input type="number" class="input-mini" id="form-add-agent03" min="300" max="850"/>
				<p class="help-block">Credit Score is optional and ranges from 300–850.</p>
			</div>
		</div>
	</fieldset>
	<fieldset class="modal-footer">
		<button href="#" class="btn" data-dismiss="modal">Close</button>
		<button type="submit" href="#" class="btn btn-primary">Save</button>
	</fieldset>
</form>