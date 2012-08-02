<?php
	// Include the header - site is setup in this file
	include( 'include-header.php' );
?>

<?php
	// Include the 'tab' pages (in bootstrap, as far as i can tell, they load at once on a page. it'd probably be nice to have true separate pages though).
	include( 'page-actionitems.php' );
	include( 'page-agents.php' );
	include( 'page-loans.php' );
	include( 'page-searchresults.php' );
?>

<?php
	//include footer - site & content is closed here.
	include( 'include-footer.php' );
?>
