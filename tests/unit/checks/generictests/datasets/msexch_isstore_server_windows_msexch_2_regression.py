#!/usr/bin/env python3
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

# fmt: off
# type: ignore

checkname = "msexch_isstore"

info = [
    [
        "Activemailboxes",
        "AverageKeywordStatsSearchExecutionTime",
        "AverageKeywordStatsSearchExecutionTime_Base",
        "AverageMultiMailboxSearchFailed",
        "AverageMultiMailboxSearchFailed_Base",
        "AverageMultiMailboxSearchQueryLength",
        "AverageMultiMailboxSearchQueryLength_Base",
        "AverageMultiMailboxSearchtimespentinFullTextIndex",
        "AverageMultiMailboxSearchtimespentinFullTextIndex_Base",
        "AverageMultiMailboxSearchtimespentinStorecalls",
        "AverageMultiMailboxSearchtimespentinStorecalls_Base",
        "AveragenumberofKeywordsinMultiMailboxSearch",
        "AveragenumberofKeywordsinMultiMailboxSearch_Base",
        "AverageSearchExecutionTime",
        "AverageSearchExecutionTime_Base",
        "Averagesearchresultsperquery",
        "Averagesearchresultsperquery_Base",
        "CachedeletesintheAddressInfocachePersec",
        "CachedeletesintheDatabaseInfocachePersec",
        "CachedeletesintheDistributionListMembershipcachePersec",
        "CachedeletesintheForeignAddressInfocachePersec",
        "CachedeletesintheForeignMailboxInfocachePersec",
        "CachedeletesintheIncompleteAddressInfocachePersec",
        "CachedeletesintheLogicalIndexcachePersec",
        "CachedeletesintheMailboxInfocachePersec",
        "CachedeletesintheOrganizationContainercachePersec",
        "CachehitsintheAddressInfocachePersec",
        "CachehitsintheDatabaseInfocachePersec",
        "CachehitsintheDistributionListMembershipcachePersec",
        "CachehitsintheForeignAddressInfocachePersec",
        "CachehitsintheForeignMailboxInfocachePersec",
        "CachehitsintheIncompleteAddressInfocachePersec",
        "CachehitsintheLogicalIndexcachePersec",
        "CachehitsintheMailboxInfocachePersec",
        "CachehitsintheOrganizationContainercachePersec",
        "CacheinsertsintheAddressInfocachePersec",
        "CacheinsertsintheDatabaseInfocachePersec",
        "CacheinsertsintheDistributionListMembershipcachePersec",
        "CacheinsertsintheForeignAddressInfocachePersec",
        "CacheinsertsintheForeignMailboxInfocachePersec",
        "CacheinsertsintheIncompleteAddressInfocachePersec",
        "CacheinsertsintheLogicalIndexcachePersec",
        "CacheinsertsintheMailboxInfocachePersec",
        "CacheinsertsintheOrganizationContainercachePersec",
        "CachelookupsintheAddressInfocachePersec",
        "CachelookupsintheDatabaseInfocachePersec",
        "CachelookupsintheDistributionListMembershipcachePersec",
        "CachelookupsintheForeignAddressInfocachePersec",
        "CachelookupsintheForeignMailboxInfocachePersec",
        "CachelookupsintheIncompleteAddressInfocachePersec",
        "CachelookupsintheLogicalIndexcachePersec",
        "CachelookupsintheMailboxInfocachePersec",
        "CachelookupsintheOrganizationContainercachePersec",
        "CachemissesintheAddressInfocachePersec",
        "CachemissesintheDatabaseInfocachePersec",
        "CachemissesintheDistributionListMembershipcachePersec",
        "CachemissesintheForeignAddressInfocachePersec",
        "CachemissesintheForeignMailboxInfocachePersec",
        "CachemissesintheIncompleteAddressInfocachePersec",
        "CachemissesintheLogicalIndexcachePersec",
        "CachemissesintheMailboxInfocachePersec",
        "CachemissesintheOrganizationContainercachePersec",
        "Caption",
        "DatabaseLevelMaintenancesPersec",
        "DatabaseState",
        "Description",
        "FolderscreatedPersec",
        "FoldersdeletedPersec",
        "FoldersopenedPersec",
        "Frequency_Object",
        "Frequency_PerfTime",
        "Frequency_Sys100NS",
        "IntegrityCheckDropBusyJobs",
        "IntegrityCheckFailedJobs",
        "IntegrityCheckPendingJobs",
        "IntegrityCheckTotalJobs",
        "LastMaintenanceItemRequestedAge",
        "Lazyindexchunkedpopulations",
        "LazyindexescreatedPersec",
        "LazyindexesdeletedPersec",
        "LazyindexfullrefreshPersec",
        "LazyindexincrementalrefreshPersec",
        "LazyindexinvalidationduetolocaleversionchangePersec",
        "LazyindexinvalidationPersec",
        "Lazyindexnonchunkedpopulations",
        "Lazyindexpopulationsfromindex",
        "Lazyindexpopulationswithouttransactionpulsing",
        "Lazyindextotalpopulations",
        "LostDiagnosticEntries",
        "MailboxesWithMaintenanceItems",
        "MailboxLevelMaintenanceItems",
        "MailboxLevelMaintenancesPersec",
        "MAPIMessagesCreatedPersec",
        "MAPIMessagesModifiedPersec",
        "MAPIMessagesOpenedPersec",
        "MessagescreatedPersec",
        "MessagesdeletedPersec",
        "MessagesDeliveredPersec",
        "MessagesopenedPersec",
        "MessagesSubmittedPersec",
        "MessagesupdatedPersec",
        "MultiMailboxKeywordStatsSearchPersec",
        "MultiMailboxPreviewSearchPersec",
        "MultiMailboxSearchFullTextIndexQueryPersec",
        "Name",
        "NonrecursivefolderhierarchyreloadsPersec",
        "Numberofactivebackgroundtasks",
        "NumberofactiveWLMLogicalIndexmaintenancetablemaintenances",
        "NumberofmailboxesmarkedforWLMLogicalIndexmaintenancetablemaintenance",
        "NumberofprocessingLogicalIndexmaintenancetasks",
        "NumberofscheduledLogicalIndexmaintenancetasks",
        "PercentRPCRequests",
        "PercentRPCRequests_Base",
        "ProcessID",
        "PropertypromotionmessagesPersec",
        "PropertypromotionsPersec",
        "PropertyPromotionTasks",
        "QuarantinedComponentCount",
        "QuarantinedMailboxCount",
        "QuarantinedSchemaUpgraderCount",
        "QuarantinedUserAccessibleMailboxCount",
        "RecursivefolderhierarchyreloadsPersec",
        "RPCAverageLatency",
        "RPCAverageLatency_Base",
        "RPCOperationsPersec",
        "RPCPacketsPersec",
        "RPCPoolContextHandles",
        "RPCPoolParkedAsyncNotificationCalls",
        "RPCPoolPools",
        "RPCRequests",
        "ScheduledISIntegDetectedCount",
        "ScheduledISIntegFixedCount",
        "ScheduledISIntegPersec",
        "SearchPersec",
        "SearchresultsPersec",
        "SizeofAddressInfocache",
        "SizeofDatabaseInfocache",
        "SizeofDistributionListMembershipcache",
        "SizeofForeignAddressInfocache",
        "SizeofForeignMailboxInfocache",
        "SizeofIncompleteAddressInfocache",
        "SizeofLogicalIndexcache",
        "SizeofMailboxInfocache",
        "SizeofOrganizationContainercache",
        "SizeoftheexpirationqueuefortheAddressInfocache",
        "SizeoftheexpirationqueuefortheDatabaseInfocache",
        "SizeoftheexpirationqueuefortheDistributionListMembershipcache",
        "SizeoftheexpirationqueuefortheForeignAddressInfocache",
        "SizeoftheexpirationqueuefortheForeignMailboxInfocache",
        "SizeoftheexpirationqueuefortheIncompleteAddressInfocache",
        "SizeoftheexpirationqueuefortheLogicalIndexcache",
        "SizeoftheexpirationqueuefortheMailboxInfocache",
        "SizeoftheexpirationqueuefortheOrganizationContainercache",
        "SubobjectscleanedPersec",
        "SubobjectscreatedPersec",
        "SubobjectsdeletedPersec",
        "Subobjectsintombstone",
        "SubobjectsopenedPersec",
        "SuccessfulsearchPersec",
        "Timestamp_Object",
        "Timestamp_PerfTime",
        "Timestamp_Sys100NS",
        "TopMessagescleanedPersec",
        "Topmessagesintombstone",
        "TotalfailedmultimailboxkeywordstatisticsSearches",
        "TotalfailedmultimailboxPreviewSearches",
        "TotalMultiMailboxkeywordstatisticssearches",
        "Totalmultimailboxkeywordstatisticssearchestimedout",
        "TotalMultiMailboxpreviewsearches",
        "Totalmultimailboxpreviewsearchestimedout",
        "TotalMultiMailboxsearchesfailedduetoFullTextfailure",
        "TotalmultimailboxsearchesFullTextIndexQueryExecution",
        "Totalnumberofsuccessfulsearchqueries",
        "Totalobjectssizeintombstonebytes",
        "Totalsearches",
        "Totalsearchesinprogress",
        "Totalsearchqueriescompletedin005sec",
        "Totalsearchqueriescompletedin052sec",
        "Totalsearchqueriescompletedin1060sec",
        "Totalsearchqueriescompletedin210sec",
        "Totalsearchqueriescompletedin60sec",
    ],
    [
        "9",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "2219184",
        "3736",
        "8803",
        "756",
        "0",
        "0",
        "0",
        "0",
        "8777",
        "10033",
        "0",
        "8331793",
        "16999241",
        "0",
        "0",
        "0",
        "0",
        "223497",
        "4021508",
        "0",
        "8811",
        "756",
        "0",
        "0",
        "0",
        "0",
        "9663",
        "10041",
        "0",
        "8344336",
        "17000070",
        "0",
        "12543",
        "10788",
        "0",
        "242823",
        "4032296",
        "0",
        "12543",
        "829",
        "0",
        "12543",
        "10788",
        "0",
        "19326",
        "10788",
        "0",
        "",
        "516",
        "1",
        "",
        "3736",
        "3736",
        "945803",
        "0",
        "2536125",
        "10000000",
        "0",
        "0",
        "0",
        "0",
        "3",
        "0",
        "7472",
        "7473",
        "3736",
        "612",
        "0",
        "3736",
        "0",
        "0",
        "0",
        "3736",
        "0",
        "0",
        "0",
        "3774",
        "15329",
        "15355",
        "232526",
        "28415",
        "2268",
        "9350",
        "234848",
        "13",
        "468",
        "0",
        "0",
        "0",
        "mailbox database 0356176343",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "50",
        "8084",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "631",
        "560849",
        "3606679",
        "5831463",
        "3606679",
        "146",
        "9",
        "67",
        "0",
        "0",
        "0",
        "0",
        "3736",
        "2219184",
        "8",
        "1",
        "0",
        "0",
        "0",
        "0",
        "0",
        "8",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "5264",
        "5257",
        "10514",
        "0",
        "5296",
        "3736",
        "0",
        "2844496046608",
        "131405402071970000",
        "2275",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "3736",
        "0",
        "3736",
        "0",
        "3736",
        "0",
        "0",
        "0",
        "0",
    ],
    [
        "9",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "2219184",
        "3736",
        "8803",
        "756",
        "0",
        "0",
        "0",
        "0",
        "8777",
        "10033",
        "0",
        "8331793",
        "16999243",
        "0",
        "0",
        "0",
        "0",
        "223497",
        "4021508",
        "0",
        "8811",
        "757",
        "0",
        "0",
        "0",
        "0",
        "9663",
        "10041",
        "0",
        "8344336",
        "17000073",
        "0",
        "12543",
        "10788",
        "0",
        "242823",
        "4032296",
        "0",
        "12543",
        "830",
        "0",
        "12543",
        "10788",
        "0",
        "19326",
        "10788",
        "0",
        "",
        "516",
        "1",
        "",
        "3736",
        "3736",
        "945803",
        "0",
        "2536125",
        "10000000",
        "0",
        "0",
        "0",
        "0",
        "3",
        "0",
        "7472",
        "7473",
        "3736",
        "612",
        "0",
        "3736",
        "0",
        "0",
        "0",
        "3736",
        "0",
        "0",
        "0",
        "3774",
        "15329",
        "15355",
        "232526",
        "28415",
        "2268",
        "9350",
        "234848",
        "13",
        "468",
        "0",
        "0",
        "0",
        "_total",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "50",
        "8084",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "631",
        "560849",
        "3606679",
        "5831463",
        "3606679",
        "178",
        "10",
        "68",
        "0",
        "0",
        "0",
        "0",
        "3736",
        "2219184",
        "8",
        "2",
        "0",
        "0",
        "0",
        "0",
        "0",
        "8",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "5264",
        "5257",
        "10514",
        "0",
        "5296",
        "3736",
        "0",
        "2844496046608",
        "131405402071970000",
        "2275",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "0",
        "3736",
        "0",
        "3736",
        "0",
        "3736",
        "0",
        "0",
        "0",
        "0",
    ],
]

discovery = {"": [("_total", None), ("mailbox database 0356176343", None)]}

checks = {
    "": [
        (
            "_total",
            {
                "store_latency": {"upper": (40.0, 50.0)},
                "clienttype_requests": {"upper": (60, 70)},
                "clienttype_latency": {"upper": (40.0, 50.0)},
            },
            [
                (
                    0,
                    "Average latency: 0.16 ms",
                    [("average_latency", 0.15550288783670518, 40.0, 50.0, None, None)],
                )
            ],
        ),
        (
            "mailbox database 0356176343",
            {
                "store_latency": {"upper": (40.0, 50.0)},
                "clienttype_requests": {"upper": (60, 70)},
                "clienttype_latency": {"upper": (40.0, 50.0)},
            },
            [
                (
                    0,
                    "Average latency: 0.16 ms",
                    [("average_latency", 0.15550288783670518, 40.0, 50.0, None, None)],
                )
            ],
        ),
    ],
}
