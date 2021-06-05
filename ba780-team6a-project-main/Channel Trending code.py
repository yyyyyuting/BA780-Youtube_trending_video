fig, ax = plt.subplots(1,2,figsize=(15.7,7.27))
df_channels = df.copy()
df_channels_trend = df_channels[df_channels['Country'] == 'United States']
df_channels_trend = df_channels_trend[['channelTitle','days_to_go_trending','publish_year','Country']]
df_channels_trend['days_to_go_trending'] = df_channels_trend['days_to_go_trending'].astype('timedelta64[D]').astype(int)
g_channels_trend = sns.distplot(df_channels_trend['days_to_go_trending'],label='United States', ax=ax[0], bins=10, color='red')
g_channels_trend.set(xlabel='Days to go trending')
g_channels_trend.legend(loc="upper right")
df_channels_trend = df_channels[df_channels['Country'] == 'Japan']
g_channels_trend1 = sns.distplot(df_channels_trend['days_to_go_trending'],label='Japan',ax=ax[1], bins=10, color='orange')
g_channels_trend1.set(xlabel='Days to go trending')
g_channels_trend1.legend(loc="upper right")          
fig.suptitle('Channels Days to go trending vs Country')

export PROJECT_ID="BA775-Team 6A"
export ZONE="us-west1-b"
export INSTANCE_NAME="python-20201020-193736"
gcloud compute ssh --project $PROJECT_ID --zone $ZONE \
  $INSTANCE_NAME -- -L 8080:localhost:8080