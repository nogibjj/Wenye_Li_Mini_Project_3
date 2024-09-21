# Wenye_Li_Individual_Project_1

## Badges

[![install](https://github.com/nogibjj/Wenye_Li_Mini_Project_3/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/Wenye_Li_Mini_Project_3/actions/workflows/install.yml)
[![format](https://github.com/nogibjj/Wenye_Li_Mini_Project_3/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/Wenye_Li_Mini_Project_3/actions/workflows/format.yml)
[![lint](https://github.com/nogibjj/Wenye_Li_Mini_Project_3/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/Wenye_Li_Mini_Project_3/actions/workflows/lint.yml)
[![test](https://github.com/nogibjj/Wenye_Li_Mini_Project_3/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/Wenye_Li_Mini_Project_3/actions/workflows/test.yml)

## Requirements

The project structure includes the following files:

- Python script (main. py)
- CI/CD with badge
- Generated summary report (PDF or markdown) via CI/CD for extra credit or making your own PDF or MD file and pushing it (summary.md)

## Dataset

| Header                    | Definition                                                                              |
| ------------------------- | --------------------------------------------------------------------------------------- |
| `alcohol-use`             | Percentage of those in an age group who used alcohol in the past 12 months              |
| `alcohol-frequency`       | Median number of times a user in an age group used alcohol in the past 12 months        |
| `marijuana-use`           | Percentage of those in an age group who used marijuana in the past 12 months            |
| `marijuana-frequency`     | Median number of times a user in an age group used marijuana in the past 12 months      |
| `cocaine-use`             | Percentage of those in an age group who used cocaine in the past 12 months              |
| `cocaine-frequency`       | Median number of times a user in an age group used cocaine in the past 12 months        |
| `crack-use`               | Percentage of those in an age group who used crack in the past 12 months                |
| `crack-frequency`         | Median number of times a user in an age group used crack in the past 12 months          |
| `heroin-use`              | Percentage of those in an age group who used heroin in the past 12 months               |
| `heroin-frequency`        | Median number of times a user in an age group used heroin in the past 12 months         |
| `hallucinogen-use`        | Percentage of those in an age group who used hallucinogens in the past 12 months        |
| `hallucinogen-frequency`  | Median number of times a user in an age group used hallucinogens in the past 12 months  |
| `inhalant-use`            | Percentage of those in an age group who used inhalants in the past 12 months            |
| `inhalant-frequency`      | Median number of times a user in an age group used inhalants in the past 12 months      |
| `pain-releiver-use`       | Percentage of those in an age group who used pain relievers in the past 12 months       |
| `pain-releiver-frequency` | Median number of times a user in an age group used pain relievers in the past 12 months |
| `oxycontin-use`           | Percentage of those in an age group who used oxycontin in the past 12 months            |
| `oxycontin-frequency`     | Median number of times a user in an age group used oxycontin in the past 12 months      |
| `tranquilizer-use`        | Percentage of those in an age group who used tranquilizer in the past 12 months         |
| `tranquilizer-frequency`  | Median number of times a user in an age group used tranquilizer in the past 12 months   |
| `stimulant-use`           | Percentage of those in an age group who used stimulants in the past 12 months           |
| `stimulant-frequency`     | Median number of times a user in an age group used stimulants in the past 12 months     |
| `meth-use`                | Percentage of those in an age group who used meth in the past 12 months                 |
| `meth-frequency`          | Median number of times a user in an age group used meth in the past 12 months           |
| `sedative-use`            | Percentage of those in an age group who used sedatives in the past 12 months            |
| `sedative-frequency`      | Median number of times a user in an age group used sedatives in the past 12 months      |

## Preparation, Checking, and Testing

- Open codespaces
- Install dependecies by using `make install` command
- Format code by using `make format` command
  ![format Image](format.png)
- Lint code by using `make lint` command
  ![lint Image](lint.png)
- Test code by using `make test` command
  ![test Image](test.png)

## Descriptive Stats and Visualizations

The descriptive statistics and vizualizations are generated through pushes via `actions-user` using `make generate_and_push` command. [descriptive statistics and vizualizations](/summary.md)
