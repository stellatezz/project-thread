# Make storage documentation usable without overstating guarantees

Status: implemented

## Problem and decision

The original README mixes setup, implementation sequence, and design history.
It also claims arbitrary-object support, directory creation, universal save safety,
and export consistency that the supplied storage module does not establish.

The [README](../../../../README.md) owns the first working example and links to
the [storage reference](../../../../docs/storage.md), which owns the API contracts
and failure behavior. Keeping everything in one README is a viable alternative
for a two-function sample, but would put detailed cleanup and durability limits
between a new reader and their first save. The separate reference adds one
navigation step and keeps those details available for lookup.

## Preserved rationale and uncertainty

The original README says a database was considered and files were chosen because
the prototype has one document. This note preserves that supplied design history;
the sample contains no decision evidence or database implementation to verify the
comparison. Revisit that choice if the product needs coordinated updates across
multiple documents. No storage architecture change is made by this documentation
revision.

There were no existing Agent Notes to supersede. The unsupported README claims
are corrected, while the original integration assumptions are explicitly marked
in the storage reference because no consumers are included.

## Verification and limits

The [evaluation record](../../../../EVALUATION.md) owns executed check results,
source-preservation evidence, and remaining verification gaps. The storage source
is unchanged. Revisit this layout when documentation grows enough to need a wider
project map; this sample does not need a new plan or roadmap hierarchy.
