# Media creation and editing

Load for persistent projects, non-trivial editing state, playback, rendering, or export. Read the product's project model, supported formats, and asset ownership before selecting a rendering stack.

## Preserve projects and edits

Separate the durable project document, source assets, editing session, playback state, and export job. Define the source of truth, project/schema version, commit points, autosave strategy, and asset references. A temporary file URL is not durable ownership. Handle missing, moved, cloud-backed, or revoked media access without silently losing edits.

Represent editing operations with meaningful undo/redo boundaries. Decide which changes form one undo step, how redo is invalidated, and how selection/playhead relate to document state. Avoid persisting transient rendering resources into the project format. Test save/reopen, interrupted saves, migration from prior projects, and recovering unsaved work according to the product promise.

## Timing and playback

Use media time representations and an explicit timebase for frame/sample operations; avoid accumulating floating-point seconds where exact boundaries matter. Specify trim endpoints, ordering, duration, audio/video sync, orientation, dimensions, color/HDR handling, and variable-frame-rate inputs as required by supported media.

Separate interactive preview quality from final export fidelity. Own observers, players, decoders, buffers, render contexts, and temporary assets with bounded lifetimes. Handle seeks and rapid edits so obsolete previews cannot replace current state. Test playback after edit/undo, timeline extremes, incompatible inputs, and interruption of audio or app activity where relevant.

Use [AVFoundation](https://developer.apple.com/documentation/avfoundation) and the actual SDK's supported media APIs; do not copy a deprecated export or composition pattern without checking availability.

## Export is its own operation

Take a defined project revision for export or explicitly define how edits during export behave. Own output path and temporary files per operation. Report preparation, rendering, finalization, cancellation, and failure accurately; a progress callback is not proof of a usable output.

Cancellation and late completion must arbitrate one outcome for the correct export. Cancelled or failed export must leave the project reopenable and clean incomplete output according to policy without deleting a later successful export or original media. Verify success by checking the actual output's playable duration, tracks, dimensions, timing, and expected edit result.

Exercise cancellation at multiple stages, low disk space, incompatible assets, failed writes, termination/relaunch, and repeated export after failure. Set memory, disk, thermal, and export-time budgets against named devices and representative durations/resolutions/track counts. Backgrounding may interrupt work; preserve recovery information and communicate resumability limits honestly.

Record a verified new-edit-operation recipe in the project's [cookbooks](../../project-thread-documentation/references/cookbooks.md), including save compatibility, undo/redo, preview, export, and failure checks.
